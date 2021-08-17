import argparse, sys

parser = argparse.ArgumentParser()

parser.add_argument('--user','-u',help="user name option",type = str)
parser.add_argument('--password','-p',help="password option",type = str)

args=parser.parse_args()

print (parser.format_help())
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://twitter.com/login")

driver.find_element_by_class_name('css-1dbjc4n r-13qz1uu').click()

username_box=driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
password_box = driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')

LOGIN_ID = "メールアドレスとかユーザ名"
PASSWORD = "パスワード"
 
def get_driver():
      
    #ヘッドレスモードでブラウザを起動
    options = Options()
    options.add_argument('--headless')
    # ブラウザーを起動
    driver = webdriver.Chrome('chromeDriver, options=options')
     
    return driver
 
# twitterログイン
def do_login(driver):
    
    # ログインURL
    get_driver("https://twitter.com/login")

    
    # 電話、メールまたはユーザー名のinput要素が読み込まれるまで待機（最大10秒）
    elem_id = WebDriverWait(driver,10).until(
        EC.visibility_of_element_located(("session[username_or_email]"))
    )
    try:
        # パスワードのinput要素
        elem_password = driver.find_element_by_name("session[password]")
   
        if elem_id and elem_password:
 
 
            # ログインID入力
            elem_id.send_keys(LOGIN_ID)
         
            # パスワード入力
            elem_password.send_keys(PASSWORD)

            # ログインボタンクリック
            elem_btn = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='LoginForm_Login_Button']"))
            )
             
            actions = ActionChains(driver)
            actions.move_to_element(elem_btn)
            actions.click(elem_btn)
            actions.perform()
             
            # 遷移
            # 遷移後のURLでログイン可否をチェック
            perform_url = driver.current_url
             
            if perform_url.find("https://twitter.com/login") == -1:
                # ログイン成功
                return True
            else:
                # ログイン失敗
                return False
                 
        else:
            return False
    except:
        return False  
 
if __name__ == "__main__":
      
    # Driver
    driver = get_driver()
 
    # ログイン
    login_flg = do_login(driver)
     
    print(login_flg)
    
driver.close