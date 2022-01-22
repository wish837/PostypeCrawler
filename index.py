from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random
import json

ID = json.load(open("config.json", "r"))["ID"]
PW = json.load(open("config.json", "r"))["PW"]

print("***********[포스타입 다운로더]***********")
time.sleep(1)

driver = webdriver.Chrome("chromedriver")

time.sleep(random.uniform(1, 3))
driver.get('https://www.postype.com/login')
time.sleep(random.uniform(1, 3))
driver.find_element_by_xpath('//*[@id="btn-sign-in-email"]').click()
time.sleep(random.uniform(1, 3))
driver.find_element_by_id('email').send_keys(ID)
time.sleep(random.uniform(1, 3))
driver.find_element_by_id('password').send_keys(PW)
time.sleep(random.uniform(1, 3))
driver.find_element_by_xpath('//*[@id="sign-in-email"]/form/div[3]/button').click()
time.sleep(random.uniform(1, 3))

while True:
    is_run = input("프로그램을 계속하기 위해선 'Y'를, 아니라면 다른 키를 눌러주세요\n: ")
    if is_run == "Y":
        POSTYPE_URL = input("다운로드할 포스트의 URL을 입력해주세요\n: ")
        FILE_NAME = input("파일을 저장할 이름을 입력해주세요\n: ")

        driver.get(POSTYPE_URL)
        time.sleep(random.uniform(1, 3))

        page = driver.page_source
        soup = BeautifulSoup(page, "html.parser")
        f = open(f"{FILE_NAME}.txt", "a", encoding="UTF8")
        for i in soup.select('#post-content'):
            data = i.get_text('\n\n', strip=True)
            f.write(data)
    else:
        print("프로그램을 종료합니다.")
        break