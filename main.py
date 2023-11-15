import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
categories = ["metallityö"]
mistakes = ["",]
for category in categories:

    driver = webdriver.Chrome()
    driver.get(f'https://www.fonecta.fi/haku/{category}')
    page_source = driver.page_source

    EMAIL_REGEX = r'''([^][()<>@,;:\\". \x00-\x1F\x7F]+|"(\n|(\\\r)*([^"\\\r\n]|\\[^\r]))*(\\\r)*")(\.([^][()<>@,;:\\". \x00-\x1F\x7F]+|"(\n|(\\\r)*([^"\\\r\n]|\\[^\r]))*(\\\r)*"))*@([^][()<>@,;:\\". \x00-\x1F\x7F]+|\[(\n|(\\\r)*([^][\\\r\n]|\\[^\r]))*(\\\r)*])(\.([^][()<>@,;:\\". \x00-\x1F\x7F]+|\[(\n|(\\\r)*([^][\\\r\n]|\\[^\r]))*(\\\r)*]))*'''

    list_of_emails = []
    driver.close()
    print(f'''
    ---------
    ---{category}---
    ---------
    ''')
    for re_match in re.finditer(EMAIL_REGEX, page_source):
        for mistake in mistakes:
            if mistake in re_match:

        list_of_emails.append(re_match.group())
    for i, email in enumerate(list_of_emails):
        print(f'{i + 1}: {email}')
