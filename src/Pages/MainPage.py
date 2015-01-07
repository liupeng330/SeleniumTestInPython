from selenium import webdriver
from Pages.BasePage import *
from Model.MediaInfo import MediaInfo
from selenium.webdriver.common.by import By

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
            contentType = r.find_element_by_class_name("list-content-type").find_elements_by_class_name("media-type")[0].text
            duration = r.find_element_by_class_name("list-content-duration").text
            contentFilesize = r.find_element_by_class_name("list-content-filesize").text
            contentDate = r.find_element_by_class_name("list-content-date").find_element_by_class_name("noListView").text
            medias.append(MediaInfo(title, contentType, duration, contentFilesize, contentDate))
        return medias