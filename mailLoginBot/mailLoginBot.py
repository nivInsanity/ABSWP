from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.get('https://account.protonmail.com/login')

#waiting only for login here, because when login is loaded - password will be loaded too :)
time.sleep(1)
nLoginElement = driver.find_element_by_xpath('//*[@id="username"]')
nLoginElement.send_keys('hornySasquatch1234@protonmail.com')

PassElem = driver.find_element_by_xpath('//*[@id="password"]')
PassElem.send_keys('twujStaryNigdyNieJestTrzezwy123)(*&^%$#@!')

loginClickButton = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/main/div[2]/form/button')
loginClickButton.click()


#TODO: Zrobić moduł, który pobiera stronę za pomocą modułu BeautifulSoup, analizuje kod, szuka stringów odpowiedzialnych
#TODO: za wprowadzanie danych, po tym podmienia kod na dane do logowania na protonmail i klika przycisk logowania

