from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

driver.get('https://account.protonmail.com/login')
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
nElement = driver.find_element_by_id('username')
print(element)

#TODO: Zrobić moduł, który pobiera stronę za pomocą modułu BeautifulSoup, analizuje kod, szuka stringów odpowiedzialnych
#TODO: za wprowadzanie danych, po tym podmienia kod na dane do logowania na protonmail i klika przycisk logowania

