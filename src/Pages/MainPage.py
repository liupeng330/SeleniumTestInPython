from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from Pages.BasePage import *
from Pages.TaskMenu import *
from Model.MediaInfo import MediaInfo

import time

class MainPage(BasePage):
    @property
    def _getRecentActivityTab(self):
        return self.driver.find_element_by_id("tab-recent")
    
    @property
    def _getMyVideosTab(self):
        return self.driver.find_element_by_id("tab-video")
    
    @property
    def _getMyCollectionsTab(self):
        return self.driver.find_element_by_id("tab-collection")
    
    @property
    def _getSharingTab(self):
        return self.driver.find_element_by_id("tab-shares")
    
    @property
    def _getBookmarksTab(self):
        return self.driver.find_element_by_id("tab-bookmarks")
    
    @property
    def _getContentRows(self):
        return self.driver.find_element_by_id("list-content-container").find_elements_by_class_name("content-row")
    
    @property
    def _getTaskMenu(self):
        return TaskMenu(self.driver)
    
    def ClickRecentActivityTab(self):
        self._getRecentActivityTab.click()
        
    def ClickMyVideosTab(self):
        self._getMyVideosTab.click()
        
    def ClickMyCollectionsTab(self):
        self._getMyCollectionsTab.click()
        
    def ClickSharingTab(self):
        self._getSharingTab.click()
    
    def ClickBookmarksTab(self):
        self._getBookmarksTab.click()
    
    def GetMediaInfos(self):
        medias = []
        for r in self._getContentRows:
            title = r.find_element_by_class_name("label-content-name").text
            duration = r.find_element_by_class_name("list-content-duration").text
            contentDate = r.find_element_by_class_name("list-content-date").find_element_by_class_name("noListView").text
            medias.append(MediaInfo(title, duration, contentDate))
        return medias
    
    def SelectMediaByName(self, name):
        #Find media by name
        media = [m.find_element_by_class_name("label-content-name") for m in self._getContentRows if m.find_element_by_class_name("label-content-name").text == name]
        if len(media) < 1:
            raise Exception("Can not find media by name '" + name + "'")
        
        #Hover it
        actionChains = ActionChains(self.driver).move_to_element(media[0])
        actionChains.perform()
        time.sleep(1)
        
        #Find displayed check box to select it
        checkBox = [m.find_element_by_class_name("list-content-selected").find_element_by_class_name("rowSelectedCheck") for m in self._getContentRows if m.find_element_by_class_name("label-content-name").text == name]
        if len(checkBox) != 1:
            raise Exception("Can not find check box by name '" + name + "'")
        checkBox[0].click()
        
    def DownloadByName(self, name):
        self.SelectMediaByName(name)
        self._getTaskMenu.ClickDownload()