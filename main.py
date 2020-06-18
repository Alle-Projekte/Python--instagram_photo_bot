import time
from selenium import webdriver

browser = webdriver.Firefox()
username = 'lockhed40'
password = '#Miami2018'

browser.get("https://www.instagram.com/")
username_field = browser.find_element_by_name('username')
password_field = browser.find_element_by_name('password')
username_field.send_keys(username)
password_field.send_keys(password)
browser.submit()
time.sleep(5)

if 'https://www.instagram.com/accounts/onetap' in browser.current_url:
    not_now = browser.find_element_by_xpath("//*[contains(text(), 'Not Now')]")
    not_now.click()
else:
    not_now = browser.find_element_by_xpath("//*[contains(text(), 'Not Now')]")
    not_now.click()
