'''Класс реализации POM для главной страницы'''

from .base_page import BasePage
from .locators import MainPageLocators
from .locators import DownloadSabyLocators

class MainPage(BasePage):
    def go_to_contacts(self):
        link = self.browser.find_element(*MainPageLocators.LOCATOR_CONTACTS_BUTTON)
        link.click()

    def dowload_saby_ver(self):
        butt = self.browser.find_element(*DownloadSabyLocators.LOCATOR_DOWNLOAD_LOCAL_VER_BUTTON)
        butt.click()

