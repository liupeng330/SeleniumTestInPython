from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from Pages.BasePage import *

class TaskMenu(BasePage):
    @property
    def _rootElement(self):
        return self.driver.find_element_by_id("fileTaskMenu")
    
    @property
    def _checkAllElement(self):
        return self._rootElement.find_element_by_id("rowSelectCheckAll")
    
    @property
    def _shareElement(self):
        return self._rootElement.find_element_by_id("taskShare")
    
    @property
    def _uploadElement(self):
        return self._rootElement.find_element_by_id("taskUpload")
    
    @property
    def _blockSenderElement(self):
        return self._rootElement.find_element_by_id("taskBlockSender")
    
    @property
    def _deleteElement(self):
        return self._rootElement.find_element_by_id("taskDelete")
    
    @property
    def _collectionElement(self):
        return self._rootElement.find_element_by_id("taskCollection")
    
    @property
    def _downloadElement(self):
        return self._rootElement.find_element_by_id("taskDownload")
    
    @property
    def _removeElement(self):
        return self._rootElement.find_element_by_id("taskRemove")
    
    @property
    def _unShareElement(self):
        return self._rootElement.find_element_by_id("taskUnShare")
    
    @property
    def _moreElement(self):
        return self._rootElement.find_element_by_id("taskMore")
    
    @property
    def _renameElement(self):
        return self._rootElement.find_element_by_id("taskRename")

    @property
    def _createCollectionElement(self):
        return self._rootElement.find_element_by_id("taskCreateCollection")
    
    @property
    def _removeShareElement(self):
        return self._rootElement.find_element_by_id("taskRemoveShare")
    
    @property
    def _showMobileShareElement(self):
        return self._rootElement.find_element_by_id("showMobileShare")
    
    def ClickShare(self):
        self._shareElement.click()
        
    def ClickDelete(self):
        self._deleteElement.click()
        
    def ClickAddToCollection(self):
        self._collectionElement.click()
        
    def ClickDownload(self):
        self._downloadElement.click()
        
    def ClickRename(self):
        self._renameElement.click()