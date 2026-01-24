from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from userinfo import username,password
import time

class Github :
    
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome()
        
    def signIn(self):
        self.browser.get("https://github.com/")
        time.sleep(2)
        WebDriverWait(self.browser,10)
        login = (self.browser.find_element(By.XPATH,"//a[@href='/login']"))
        login.click()
        usernameInput = self.browser.find_element(By.NAME,"login")
        passwordInput = self.browser.find_element(By.NAME,"password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        passwordInput.send_keys(Keys.ENTER)
   
        self.browser.find_element(By.NAME,"button").click()

        WebDriverWait(self.browser,10)

        ul = list(self.browser.find_elements(By.CLASS_NAME,"js-repos-container"))
        WebDriverWait(self.browser,10)
        for li in ul:
            WebDriverWait(self.browser,10)
            a = li.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
            print(a.title())
        time.sleep(3)
        
        
        
user = Github(username,password)

print(user.signIn())