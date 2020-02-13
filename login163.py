# coding=utf-8

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.126.com")

current_window = driver.current_window_handle

time.sleep(3)

driver.find_element_by_link_text('密码登录').click()

fname = driver.find_element_by_tag_name("iframe")
driver.switch_to_frame(fname)
driver.find_element_by_name('email').send_keys("feifutureai")
driver.find_element_by_name('password').send_keys("13524226605")
driver.find_element_by_id("dologin").click()

#driver.find_element_by_id('_mail_component_15_15').click()

#all_windows = driver.window_handles
#for window in all_windows:
#    if window != current_window:
#        driver.switch_to_window(window)
#current_window = driver.current_window_handle

driver.implicitly_wait(60)

time.sleep(60)
driver.refresh()

print(driver.current_url)
