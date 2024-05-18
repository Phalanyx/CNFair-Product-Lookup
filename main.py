from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
import csv


driver = webdriver.Chrome() 


def write_output(url):
    driver.get(url)   
    time.sleep(0.5)
    status = driver.find_elements(By.CLASS_NAME, 'detail-Container.container')
    for x in status:
        first = x.find_elements(By.CLASS_NAME, 'product-attr')
        second_name = x.find_elements(By.CLASS_NAME, 'title')
        for item in first:
            check = item.find_elements(By.CLASS_NAME, 'exchange.btn.btn-primary')
    if (len(second_name) == 0 or len(first) == 0):
        return
    for x in second_name:
        item_name = x.find_elements(By.TAG_NAME, "span")
    for x in item_name:
        new_item = x.text
    for x in check:
        item_status = x.text
    if (item_status != "Stay tuned"):
        return
    seller_name = driver.find_elements(By.CLASS_NAME, 'store-name.ellipsis')
    for x in seller_name:
        seller_user = x.text
    f = open('output3.csv', 'a', newline='', encoding='utf-8-sig')
    print(seller_user)
    row = (new_item, seller_user, url)
    writer = csv.writer(f)
    writer.writerow(row)
    f.close()

random = 1016
url = 'https://cnfair.com/detail/PI2401000'
new_url = url + str(random)

for x in range(random, random + 10000):
    new_url = url + str(x)
    write_output(new_url)