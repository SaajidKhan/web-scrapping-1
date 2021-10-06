from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

start_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.chrome("D:\DO NOT DELETE\Downloads\chromedriver_win32")
browser.get(start_url)
time.sleep(10)

def scrap():
    headers=["name","distance","mass","radius"]
    star_data=[]
    for i in range(1,23):
        soup=BeaytifulSoup(browser.page_source,"html.parser")
        