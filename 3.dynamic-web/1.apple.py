from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv

driver = webdriver.Chrome()
URL = 'https://music.apple.com/kr/playlist/%EC%98%A4%EB%8A%98%EC%9D%98-top-100-%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD/pl.d3d10c32fbc540b38e266367dc8cb00c'
driver.get(URL)

time.sleep(5)  # 페이지가 로드될 시간

# 곡 리스트 전체 가져오기
tracks = driver.find_elements(By.CSS_SELECTOR, 'div.songs-list-row')  # 예시 CSS 선택자. 실제 구조 보고 확인 필요

track_ranking_data = []

for i, track in enumerate(tracks[:10]):  # 예: 상위 10개만 가져오기
    try:
        title = track.find_element(By.CSS_SELECTOR, '.songs-list-row__song-name').text
        artist = track.find_element(By.CSS_SELECTOR, '.songs-list__col.songs-list__col--artist').text
        # 날짜 정보는 없을 수 있음. 애플 뮤직 구조에 따라 다름
        publish_date = ""  # 대체할 정보로 수정 가능

        track_ranking_data.append([i + 1, title, artist, publish_date])
    except Exception as e:
        print(f"Error parsing track {i+1}: {e}")

# 저장 경로
local_file_path = '/home/ubuntu/damf2/data/apple/'

def save_to_csv(data):
    with open(local_file_path + 'apple-top-100.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Rank', 'Title', 'Artist', 'Publish Date'])  # 헤더
        writer.writerows(data)

save_to_csv(track_ranking_data)

driver.quit()
