import argparse, sys

parser = argparse.ArgumentParser()

parser.add_argument('--user','-u',help="user name option",type = str)
parser.add_argument('--password','-p',help="password option",type = str)

args=parser.parse_args()

print (parser.format_help())
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

# ユーザー名/メールアドレス
username = input("mail-address:")
#パスワード
password = input("password:")

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://twitter.com/login")

driver.find_element_by_class_name('css-1dbjc4n r-13qz1uu').click()
time.sleep(3)
username_box=driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
password_box = driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')

# ユーザ名とパスワードをインプットする
username_box.send_keys(username)
password_box.send_keys(password)

# ログインボタンを探す
login_button = driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')
#ログインボタンをクリック
login_button.click()