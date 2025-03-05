'''Класс с тест-кейсом №3 (бизнес-логика)'''

import time
from pages_and_related_files.main_page import MainPage
from pages_and_related_files.dowload_ver_page import DownloadFiles

from pages_and_related_files.locators import (
    MainPageLocators, DownloadSabyLocators)

class TestCase3():

    def test_link_saby(self, browser):
        page = MainPage(browser, MainPageLocators.MAIN_LINK)
        page.open_site()
        page.dowload_saby_ver()
        time.sleep(1)
        linkdowload = DownloadFiles(browser, browser.current_url)
        downlad_link = MainPage(browser, DownloadSabyLocators.LOCATOR_DOWLOAD_LINK_MY_VER)
        downlad_link.open_site()
        linkdowload.size_web_file_info()
