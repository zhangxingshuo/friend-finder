'''
Uses a headless webdriver to scroll through a given profile's friend list and 
extract the final html file
'''

from selenium import webdriver

import time
from login_info import username, passwd

# dest_url = 'https://www.facebook.com/andy97zhang/friends?source_ref=pb_friends_tl' me
# dest_url = 'https://www.facebook.com/profile.php?id=100010071934418&sk=friends&source_ref=pb_friends_tl' lilly
dest_url = 'https://www.facebook.com/nathan.justin.14/friends?source_ref=pb_friends_tl' # nathan

driver = webdriver.Firefox()
driver.get('https://www.facebook.com/')
print("Opened facebook...")
a = driver.find_element_by_id('email')
a.send_keys(username)
print("Email entered...")
b = driver.find_element_by_id('pass')
b.send_keys(passwd)
print("Password entered...")
c = driver.find_element_by_id('loginbutton')
c.click()
time.sleep(3)
driver.get(dest_url)
time.sleep(3)
lastHeight = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    newHeight = driver.execute_script("return document.body.scrollHeight")
    if newHeight == lastHeight:
        break
    lastHeight = newHeight
html_source = driver.page_source
print(html_source)
open('sel_out.txt','w').write(html_source)
driver.quit()