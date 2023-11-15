import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
#,"rakennusala","metalli","metallityö"
categories = ["metallityö"]

for category in categories:
    driver = webdriver.Chrome()

    driver.get(f'https://www.fonecta.fi/haku/{category}')
    page_source = BeautifulSoup(driver.page_source,'html.parser')
    print(page_source.find_all('a',class_='ResultItemComponent_resultItemLink__PV_3y ResultItemComponent_resultItemName__cciXV'))

    #url = f'https://www.fonecta.fi/haku/{category}'
    #req = requests.get(url)
    #soup = BeautifulSoup(req.content, 'html.parser')
    #contacts = page_source.find_all("a", class_="ResultItemComponent_resultItemLink__PV_3y ResultItemComponent_resultItemName__cciXV")
    #print(contacts)
    #for contact in contacts:
        #print(contact.get('href'))

