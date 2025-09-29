#two types button pagination
#one: on-load pagination
#two: on-render pagination
#scroll pagination
#show more/next pagination

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.daraz.com.bd/hoses-pipes')
driver.maximize_window()
text_list = []
for i in range(1,41):
    j = str(i)
    text = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+j+']/div/div/div[2]/div[2]/a').text
    text_list.append(text_list)


print(text_list)

time.sleep(20)
driver.quit()