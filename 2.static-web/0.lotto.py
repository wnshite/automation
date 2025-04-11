import requests
from bs4 import BeautifulSoup

lotto_url = 'https://dhlottery.co.kr/common.do?method=main' # 동행복권 사이트 메인페이지 가져오기

res = requests.get(lotto_url)

soup = BeautifulSoup(res.text, 'html.parser')

balls = soup.select('span.ball_645')
for ball in balls:
    print(ball.text) # balls의 텍스트만 출력