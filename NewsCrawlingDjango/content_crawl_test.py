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

#chrome driver 설정
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
options.add_argument('lang=ko_KR')
driver = webdriver.Chrome(options=options)

def content_crawl(url):
    driver.get(url)
    time.sleep(0.5)
    try:
        driver.find_element_by_xpath('//*[@id="ct"]/div[1]/div[3]/div[3]/div[2]/div[1]/a').click()
        #//*[@id="ct"]/div[1]/div[3]/div[3]/div[2]/div[1]/a
        #//*[@id="main_content"]/div[1]/div[3]/div/div[3]/div[2]/div[1]/a
    except :
        print(url)
    finally:
        time.sleep(5)
        #Beautifulsoup 생성
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        #데이터 크롤
        # Date = soup.select_one("span.t11")
        # Date=str(Date)
        # Date=Date[18:]
        # Date=Date[:-7]
        #Title = soup.find('h3',id="articleTitle")
        Title = soup.select_one("#ct > div.media_end_head.go_trans > div.media_end_head_info.nv_notrans > div.media_end_head_info_variety > div.media_end_head_info_variety_right > div.media_end_head_autosummary._auto_summary_wrapper._SUMMARY._LIKE_HIDE > div.media_end_head_autosummary_layer._auto_summary_contents._SUMMARY_LAYER > div.media_end_head_autosummary_layer_body > div > strong")
        Title=str(Title)
        Title=Title[53:]
        Title=Title[:-9]
        Summary = soup.select_one("#ct > div.media_end_head.go_trans > div.media_end_head_info.nv_notrans > div.media_end_head_info_variety > div.media_end_head_info_variety_right > div.media_end_head_autosummary._auto_summary_wrapper._SUMMARY._LIKE_HIDE > div.media_end_head_autosummary_layer._auto_summary_contents._SUMMARY_LAYER > div.media_end_head_autosummary_layer_body > div")
        Summary=str(Summary)
        Summary=Summary[50:]
        Summary=Summary[:-6]

        print(Title)
        print(Summary)
        

content_crawl('https://n.news.naver.com/mnews/article/469/0000674672')