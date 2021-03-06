from django.shortcuts import render
from rest_framework import viewsets
from crawled_data.serializers import  UserInputSerializer, BoardDataSerializer, CrawlDataSerializer
from crawled_data.models import UserInput, BoardData, CrawlData

from tabnanny import process_tokens
from urllib.parse import quote_plus    
from selenium import webdriver    
from bs4 import BeautifulSoup
import requests
import datetime
from multiprocessing import Pool
from konlpy.tag import Hannanum
from wordcloud import WordCloud, STOPWORDS

from crawled_data.models import BoardData

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
options.add_argument('lang=ko_KR')
driver = webdriver.Chrome(options=options)

class BoardDataViewSet(viewsets.ModelViewSet):
    serializer_class = BoardDataSerializer
    queryset = BoardData.objects.all()

class CrawlDataViewSet(viewsets.ModelViewSet):
    serializer_class = CrawlDataSerializer
    queryset = CrawlData.objects.all()

class UserInputViewSet(viewsets.ModelViewSet):
    serializer_class = UserInputSerializer
    queryset = UserInput.objects.all()

    def perform_create(self, serializer):
        def url_crawl(dateList):
            url_list = list()

            for date in dateList:     
                OID = ['032','005','020','021','022','023','025','028','469']
                for i in range(0,9,1):
                    url = "https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&oid={}&date={}".format(OID[i], date)
                    req = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
                    html = req.text
                    soup = BeautifulSoup(html, 'html.parser')

                    for link in soup.find_all('a',{'class' : 'nclicks(cnt_flashart)'}):
                        row=link.get('href')
                        url_list.append(row)

            return url_list
        
        def content_crawl(url):
            req = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')

            Date = soup.select_one('#ct > div.media_end_head.go_trans > div.media_end_head_info.nv_notrans > div.media_end_head_info_datestamp > div > span')
            Date=str(Date)
            Date = Date[105:]
            Date = Date[:-7]

            Title = soup.select_one('#ct > div.media_end_head.go_trans > div.media_end_head_title > h2')
            Title = str(Title)
            Title=Title[36:]
            Title=Title[:-5]

            row = []
            row.append(Date)
            row.append(Title)
            row.append(url)
            return row

        def word_count(data):
            hannanum = Hannanum()
            t_noun= {}
            Title = []

            for line in data:
                Title.append(str(line[1]))
            
            for i in Title:
                tmp = hannanum.nouns(i)
                for noun in tmp:
                    if noun in t_noun:
                        t_noun[noun] = t_noun[noun] + 1
                    else:
                        t_noun[noun] = 1
            
            return t_noun
        
        def find_url(words, news):
            a = dict()
            b = dict()
            for word in words:
                for line in news:
                    if (word in line[1]) and not (line[1] in b.values()):
                        a[word] = line[2]
                        b[word] = line[1]
                        break
            return a,b
        
        crawled_data = []

        input_start_date = serializer.validated_data['startdate']
        input_finish_date = serializer.validated_data['finishdate']
        startdate = datetime.date(int(input_start_date[0:4]), int(input_start_date[4:6]), int(input_start_date[6:8]))
        finishdate = datetime.date(int(input_finish_date[0:4]), int(input_finish_date[4:6]), int(input_finish_date[6:8]))

        day_count = (finishdate - startdate).days + 1
        dList = []
        news_data=[]
        for d in (startdate + datetime.timedelta(n) for n in range(day_count)):
            date = str(d)
            date = str(date[0:4]) + str(date[5:7]) +str(date[8:10])
            news = CrawlData.objects.filter(date = date)
            cnt = news.count()
            if cnt == 0:
                dList.append(date)
            else:
                for line in news:
                    news_data.append((line.date, line.title, line.url))


        if len(dList) != 0 :
            url_list = url_crawl(dList)
            for url in url_list:
                crawled_data.append(content_crawl(url))
                    
            for line in crawled_data:
                if (not line[0]=='') and (not line[1]==''):
                    news_data.append((line[0], line[1], line[2]))
                    d=line[0]
                    d = str(d[0:4]) + str(d[5:7]) +str(d[8:10])
                    CrawlData(date = d, title = line[1], url = line[2]).save()
        # pool = Pool(processes=16)
        # crawled_data.append(pool.map(content_crawl, url_crawl(startdate, finishdate)))

        

        cloud_data = word_count(news_data)
        xList = ['??????','??????','??????','[??????]','[??????]','[??????]']
        for word in xList:
            if word in cloud_data.keys():
                cloud_data[word]=0
        
        spwords = set(STOPWORDS)
        spwords.add('??????')
        spwords.add('[??????]')
        spwords.add('??????')
        spwords.add('[??????]')
        spwords.add('??????')
        spwords.add('[??????]')
        wc = WordCloud(max_font_size=150, stopwords = spwords, background_color = 'white', font_path='crawled_data/font/DX.ttf', width = 1000, height = 800).generate_from_frequencies(cloud_data)
        wc.to_file('cloud.jpg')

        sorted_dict = sorted(cloud_data.items(), key = lambda item: item[1], reverse = True)
        word_to_find = [sorted_dict[0][0], sorted_dict[1][0], sorted_dict[2][0]]

        url_list, title_list = find_url(word_to_find, news_data)
        BoardData(start = input_start_date,
            finish = input_finish_date,
            word1 = word_to_find[0],
            title1 = title_list[word_to_find[0]],
            link1 = url_list[word_to_find[0]],
            word2 = word_to_find[1],
            title2 = title_list[word_to_find[1]],
            link2 = url_list[word_to_find[1]],
            word3 = word_to_find[2],
            title3 = title_list[word_to_find[2]],
            link3 = url_list[word_to_find[2]],
            cloud = './cloud.jpg').save()

        serializer.save(startdate = input_start_date)
        serializer.save(finishdate = input_finish_date)
