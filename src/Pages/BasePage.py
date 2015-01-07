from selenium import webdriver

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver