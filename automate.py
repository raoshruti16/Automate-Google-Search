# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver
browser = webdriver.Chrome('C:\chromedriver_win32\chromedriver')
browser.get('http://www.google.com') 
elem = browser.find_element_by_name('q')
elem.send_keys('Akshay Kumar')
from selenium.webdriver.common.keys import Keys
elem.send_keys(Keys.ENTER)