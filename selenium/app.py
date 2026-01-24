from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from userinfo import username,password

class Github :
    
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome()
        
    def signIn(self):
        self.browser.get("https://github.com/")
        login = self.browser.find_element(By.CSS_SELECTOR,"")
        login.click()
        
    def repo(self):
        pass
    
    def profil(self):
        pass
        
        