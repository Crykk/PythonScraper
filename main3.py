import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re

def launchBrowser():
   driver = webdriver.Chrome()

   driver.get(f'https://www.fonecta.fi/haku/metallityö')
   page_source = BeautifulSoup(driver.page_source, 'html.parser')
   print(page_source.find_all('a',
                              class_='ResultItemComponent_resultItemLink__PV_3y ResultItemComponent_resultItemName__cciXV'))

   driver.get("http://www.google.com/")
   while(True):
       pass
launchBrowser()