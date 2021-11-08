# import requests
# from bs4 import BeautifulSoup as bs

# Obtain a list of all cars for sale from http://www.ss.com from a make of your choosing(VW, BMW, etc) and save as an
# JSON, CSV or xlsx file.
#
# Alternative, get a list of apartments for rent in a certain region.
#
# You can also browse through a wikipedia page of your choice and perform some actions(click,get element contents) of
# your choice.
#
# Bonus. Write tests that check whether you received sane values.
# Example tests could be whether you receive at least one row of data.

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time
import json

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get('https://www.ss.com/')
time.sleep(5)
cars_element = driver.find_element_by_id("mtd_97")
cars_element.click()

subaru = driver.find_element_by_id("ahc_159")
page_title = subaru.get_attribute('title')
page_title = ''.join([i for i in page_title if i.isalpha()])
subaru.click()

table_rows = driver.find_elements_by_tag_name("tr")
# print("Found", len(table_rows), "elements")

ad_rows = [row for row in table_rows if row.get_attribute("id") and row.get_attribute("id").startswith("tr_")]
add_text = [[add.text] for add in ad_rows]
# print(add_text)

headline = driver.find_element_by_id("head_line")
head_cells = headline.find_elements_by_tag_name("td")
header_text = [add.text for add in head_cells]
# print(header_text)

if len(add_text) >= 1:
    print(f"Found {len(add_text)} ads")
    with open(f"{page_title}.json", mode="w", encoding="UTF-8") as write_file:
        json.dump([header_text] + add_text, write_file, indent=4)
else:
    print("Insufficient amount of data found!")
