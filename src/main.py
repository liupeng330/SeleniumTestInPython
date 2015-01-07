from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from Pages import *

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

login = SignIn.SignIn(driver)
mainPage = MainPage.MainPage(driver)

# Go to the cloud signin page
print "Load sign in page"
driver.get("https://cloud.real.com/account/auth")
driver.maximize_window()

# Login
print "Login"
login.Login("pengliu@realnetworks.com", "123456")

try:
    print "Wait main page loaded"
    WebDriverWait(driver, 10).until(EC.title_contains("RealPlayer Cloud - Your videos, always available"))
    
    print "Wait list content container appear"
    WebDriverWait(driver, 1000 * 60 * 5).until(EC.presence_of_element_located((By.ID, "list-content-container")), "Wait list-content-container appear")
    
    print "Click 'My Videos' tab"
    mainPage.ClickMyVideosTab()
    
    print mainPage.GetMediaInfos()
    
finally:
    pass
    #driver.quit()