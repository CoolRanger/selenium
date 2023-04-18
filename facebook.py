from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


options = Options()
options.add_argument('--ignore-certificate-errors')

driver_service = Service(executable_path=PATH)

driver = launchBrowser()
driver.get('https://www.youtube.com/')
WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inline-preview-player"]/div[15]/div[1]'))).click()