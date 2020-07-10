# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver
import time
browser = webdriver.Chrome('C:\chromedriver_win32\chromedriver')
browser.get('http://www.google.com') 
elem = browser.find_element_by_name('q')
elem.send_keys('Continuum')
from selenium.webdriver.common.keys import Keys
elem.send_keys(Keys.ENTER)
time.sleep(3)
link = browser.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/a/h3')
link.click()
