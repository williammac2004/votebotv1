import random
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.proxy import Proxy, ProxyType
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy

x = 0

y = input("How many votes would you like to place? ")
gap = input("How long would you like to wait between each vote? (S) ")

while x < int(y):
	PROXY = random.choice(open('proxies.txt').readlines())

	webdriver.DesiredCapabilities.CHROME['proxy']={
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY, 
    "proxyType":"MANUAL",
}
# 1000 over saturday and subnday
	print(PROXY)

	try:
		driver = webdriver.Chrome(executable_path= r"/Users/will/Desktop/chromedriver")

		driver.get('https://www.innovatefinance.com/pitch360heats/')

		select = Select(driver.find_element_by_xpath('//*[@id="wpcf7-f351155-p351095-o7"]/form/p[1]/span/select'))

		# select by visible text
		select.select_by_visible_text('BlueFire AI')

		driver.find_element_by_xpath("//*[@id=\"wpcf7-f351155-p351095-o7\"]/form/p[2]/input").click()

		time.sleep(10)

		driver.close()

		time.sleep(int(gap))

		x += 1
	except:
		print("Broken Proxy. Trying again... ")








