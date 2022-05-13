from tabnanny import process_tokens
from urllib.parse import quote_plus    # 한글 텍스트를 퍼센트 인코딩으로 변환
from selenium import webdriver    # 라이브러리에서 사용하는 모듈만 호출
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 해당 태그를 기다림
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException    # 태그가 없는 예외 처리
import time
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import datetime
from multiprocessing import Pool

global crawled_data
crawled_data = list()

#chrome driver 설정
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
options.add_argument('lang=ko_KR')
driver = webdriver.Chrome(options=options)


# 언론사별 10개씩 크롤링
# 신문사별 oid
# 경향신문 032
# 국민일보 005
# 동아일보 020
# 문화일보 021
# 서울신문 081  --> 제외 :  요약 기능 x
# 세계일보 022
# 조선일보 023
# 중앙일보 025
# 한겨례 028
# 한국일보 469

OID = ['032','005','020','021','022','023','025','028','469']

def url_crawl(startdate, finishdate):
    # fd = open('url.csv', 'w', encoding='utf-8', newline='')
    # wr = csv.writer(fd)
    # wr.writerow(['url'])
    url_list = list()
    day_count = (finishdate - startdate).days + 1

    for d in (startdate + datetime.timedelta(n) for n in range(day_count)):
        date = str(d)
        date = str(date[0:4]) + str(date[5:7]) +str(date[8:10])

        for i in range(0,9,1):
            url = "https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&oid={}&date={}".format(OID[i], date)
            req = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')

            for link in soup.find_all('a',{'class' : 'nclicks(cnt_flashart)'}):
                row=link.get('href')
                url_list.append(row)
                # temp = [row]
                # wr.writerow(temp)

    # fd.close()
    print(url_list)
    print('url crawling finish')
    return url_list




def content_crawl(url):
    #뉴스기사 저장용 csv 파일 생성
    #fd = open('output.csv', 'w', encoding='utf-8-sig', newline='')
    #wr = csv.writer(fd,delimiter=',')
    # wr.writerow(['Date','Title','Summary'])
    #wr.writerow(['Title','Summary'])
    #wr.writerow(['Title','URL'])


    #url별로 뉴스 크롤링
    #selenium
    # driver.get(url)
    # time.sleep(0.5)
    # try:
    #     driver.find_element_by_xpath('//*[@id="ct"]/div[1]/div[3]/div[3]/div[2]/div[1]/a').click()
    #     #//*[@id="ct"]/div[1]/div[3]/div[3]/div[2]/div[1]/a
    #     #//*[@id="main_content"]/div[1]/div[3]/div/div[3]/div[2]/div[1]/a
    # except :
    #     print(url)
    # finally:
    #     time.sleep(5)
    #     print('crawl start > '+ str(url) + ' >', end='')
    #     #Beautifulsoup 생성
    #     html = driver.page_source
    #     soup = BeautifulSoup(html, 'html.parser')

    #     #데이터 크롤
    #     # Date = soup.select_one("span.t11")
    #     # Date=str(Date)
    #     # Date=Date[18:]
    #     # Date=Date[:-7]
    #     #Title = soup.find('h3',id="articleTitle")
    #     Title = soup.select_one("#ct > div.media_end_head.go_trans > div.media_end_head_info.nv_notrans > div.media_end_head_info_variety > div.media_end_head_info_variety_right > div.media_end_head_autosummary._auto_summary_wrapper._SUMMARY._LIKE_HIDE > div.media_end_head_autosummary_layer._auto_summary_contents._SUMMARY_LAYER > div.media_end_head_autosummary_layer_body > div > strong")
    #     Title=str(Title)
    #     Title=Title[53:]
    #     Title=Title[:-9]
    #     Summary = soup.select_one("#ct > div.media_end_head.go_trans > div.media_end_head_info.nv_notrans > div.media_end_head_info_variety > div.media_end_head_info_variety_right > div.media_end_head_autosummary._auto_summary_wrapper._SUMMARY._LIKE_HIDE > div.media_end_head_autosummary_layer._auto_summary_contents._SUMMARY_LAYER > div.media_end_head_autosummary_layer_body > div")
    #     Summary=str(Summary)
    #     Summary=Summary[50:]
    #     Summary=Summary[:-6]

    #     #csv에 저
    #     row = []
    #     # row.append(Date)
    #     row.append(Title)
    #     row.append(Summary)
    #     wr.writerow(row)
    #     print('crawl end')
    # driver.get(url)
    # time.sleep(0.5)
    # html = driver.page_source
    # soup = BeautifulSoup(html, 'html.parser')

    req = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    Title = soup.select_one('#ct > div.media_end_head.go_trans > div.media_end_head_title > h2')
    Title = str(Title)
    Title=Title[36:]
    Title=Title[:-5]
    row = []
    row.append(Title)
    row.append(url)
    crawled_data.append(row)
    print(row)
    #wr.writerow(row)
    #csv 닫기
    #fd.close()




if __name__=='__main__':
    #날짜 설정
    input_start_date = input('시작 날짜를 입력하세요(YYYYMMDD) : ')
    startdate = datetime.date(int(input_start_date[0:4]), int(input_start_date[4:6]), int(input_start_date[6:8]))
    input_finish_date = input('끝나는 날짜를 입력하세요(YYYYMMDD) : ')
    finishdate = datetime.date(int(input_finish_date[0:4]), int(input_finish_date[4:6]), int(input_finish_date[6:8]))

    pool = Pool(processes=8)
    pool.map(content_crawl, url_crawl(startdate, finishdate))
    #프로그램 종료
    for line in crawled_data:
        print(line)
    print('content crawling finish')
    
