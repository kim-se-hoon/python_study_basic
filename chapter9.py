''' 표준 라이브러리 '''

import datetime
day1 = datetime.date(2025, 6, 7)
day2 = datetime.date(2025, 6, 24)
days = day2 - day1
print(days.days)

print(day1.weekday())
print(day2.weekday())
# 월요일 -> 0

import time
a = time.time()
print(a)
# 1970년 1월 1일 0시 0분 0초 기준(협정세계 표준시)으로 지난 초단위
print(time.ctime())

# for i in range(5):
#     print(i)
#     time.sleep(1)

# import random
# print(random.random())
# print(random.randint(1, 45))

''' 크롤링 '''
import requests
# url = "https://www.naver.com/"
# response = requests.get(url)
# print("응답코드:", response.status_code)
# print(response.text)

# url = "https://search.naver.com/search.naver"
# param = {"query": "강아지"}
# response = requests.get(url, params=param)
# print(response.text)

'''
BeautifulSoup 메소드 활용하기
1. find(): 지정된 태그들 중에 가장 첫번째 태그만 가져오는 메소드
2. find_all(): 지정된 태그들 전부 가져오는 메소드
3. 클래스 속성을 활용하는 방법
  1) soup.find_all('태그명', class='클래스명')
  2) soup.find('태그명', id='id명')
'''
import urllib.request
from bs4 import BeautifulSoup
webpage = urllib.request.urlopen("https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=6&acq=%EC%A0%9C%EC%A3%BC%EB%82%A0%EC%94%A8&qdt=0&ie=utf8&query=%EC%A0%9C%EC%A3%BC%EB%82%A0%EC%94%A8&ackey=g2dx52h7")
soup = BeautifulSoup(webpage, 'html.parser')
# print(soup)
temps = soup.find('strong', '')
print(temps.get_text())

htemps = soup.find('dd', 'desc')
print("체감온도: ", htemps.get_text())
print()
webpage2 = urllib.request.urlopen("https://www.netflix.com/kr/")
soup2 = BeautifulSoup(webpage2, 'html.parser')
# print(soup2)
title = soup2.find_all('div', class_="default-ltr-cache-3xjlkv e1rogofe1")

for i in range(len(title)):
    print(title[i].get_text())