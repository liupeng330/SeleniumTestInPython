from selenium import webdriver
from Pages.BasePage import *

class SignIn(BasePage):
    def _getUserName(self):
        return self.driver.find_element_by_name("username");
    
    def _getPassword(self):
        return self.driver.find_element_by_name("password");
    
    def _getLogin(self):
        return self.driver.find_element_by_id("rpLoginAccount");
    
    def Login(self, username, password):
        self._getUserName().send_keys(username)
        self._getPassword().send_keys(password)
        self._getLogin().click()