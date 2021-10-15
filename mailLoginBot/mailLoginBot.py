import requests

from bs4 import BeautifulSoup

from selenium import webdriver

print('Za warudo')

driver = webdriver.Firefox()

driver.get('https://protonmail.com/pl/')

#TODO: Zrobić moduł, który pobiera stronę za pomocą modułu BeautifulSoup, analizuje kod, szuka stringów odpowiedzialnych
#TODO: za wprowadzanie danych, po tym podmienia kod na dane do logowania na protonmail i klika przycisk logowania

#Request nie daje sobie z tym rady - pobiera tylko html, a potrzebujemy elementów JS, trzeba spróbować pobrać html za pomocą selenium