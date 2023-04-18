from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

image = "https://imgur.com/js7ArJV"
current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
target_time = '2023-04-16 03:00:00'

options = Options()
prefs = {
    'profile.default_content_setting_values' :
        {
        'notifications' : 2
         }
}
options.add_experimental_option('prefs', prefs)
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.get('https://www.facebook.com')
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('kevin.wu0904@yahoo.com.tw')
driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys('9494kevin', '\ue007')
#WebDriverWait(driver, 20).until(EC.visibility_of_element_located((')).click()
#print("已打开Messenger")
#driver.find_element(By.NAME, 'login').click()
time_difference = (time.mktime(time.strptime(target_time, '%Y-%m-%d %H:%M:%S')) -
                  time.mktime(time.strptime(current_time, '%Y-%m-%d %H:%M:%S')))
if time_difference>0:
    print("等待中....")
    time.sleep(time_difference)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Messenger"]'))).click()
search_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="搜尋 Messenger"]')))
time.sleep(2)
search_name.send_keys('2024')


uglyman = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, '6069461506473378')))
uglyman.click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="訊息"]'))).send_keys(image, '\ue007')

#WebDriverWait(driver, 10, 0.2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mount_0_0_Us"]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span'))).click()


