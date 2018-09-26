from selenium import webdriver
from contextlib import contextmanager
import time

browser = webdriver.Firefox()

browser.get("https://www.linkedin.com/")
#waiting users for logging in
time.sleep(30)

browser.get("https://www.linkedin.com/mynetwork/")
time.sleep(5)

a = 1
#Linkedin allows just 30 thousand connections for free users
while a < 30000:
	#Connection request will be sent automatically for each suggestions		
	connect = browser.find_element_by_xpath("/html/body/div[5]/div[5]/div[2]/div/div/div/div/div/div/div/section/ul/li[1]/div/section/footer")
	connect.click()
	time.sleep(1)
	#Window should be scrolled for more suggestions 
	browser.execute_script("window.scrollTo(0,20000000);")
	time.sleep(2)
	browser.execute_script("window.scrollTo(0,20);")
	time.sleep(1)
	a = a+1