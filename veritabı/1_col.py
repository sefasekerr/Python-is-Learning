from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait

driver = webdriver.Chrome()
import time
driver.get("https://www.turkiye.gov.tr/doviz-kurlari")
time.sleep(2)
driver.find_elements(By.CLASS_NAME,"tableWrapper")
i = list(driver.find_elements(By.CSS_SELECTOR,"tbody tr"))



# driver.find_element(By.CSS_SELECTOR,"tbody")
for e in i:
    print(e.text)

WebDriverWait(driver,10)
# inp.send_keys(Keys.ENTER)

# time.sleep(5)
# login = driver.find_element(By.PARTIAL_LINK_TEXT,("Oturum aç")).click()
# time.sleep(5)

