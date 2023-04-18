from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs) 
options.add_argument("disable-infobars") 

driver = webdriver.Chrome(options=options)
driver.maximize_window() 

driver.get("https://m.momoshop.com.tw/mymomo/login.momo") # 到登入頁面

driver.find_element_by_id('memId').send_keys('帳號') # 輸入帳號
driver.find_element_by_id('passwd').send_keys('密碼') # 輸入密碼
driver.find_element_by_class_name('login').click()

driver.get("https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=8267514&str_category_code=2900100474")
#driver.get("https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=8820259&mdiv=shopCart")

while 1:
    try:
        buy = WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located((By.ID, 'buy_yes'))) # 顯性等待
        buy.click() # 偵測到可以購買按鈕就點擊按鈕
        print ('可以購買!')
        break # 後面結帳部分就不寫囉
    except:
        print("還不能購買! 重新整理!")
        driver.refresh() # 重整頁面