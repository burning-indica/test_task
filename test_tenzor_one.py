'''Класс с тест-кейсом №1 (бизнес-логика)'''

import time
from pages_and_related_files.contact_page import ContactsPage
from pages_and_related_files.tenzor_page import TenzPage
from pages_and_related_files.about_page import AboutPage
from pages_and_related_files.locators import (
    MainPageLocators, TenzPageLocators, AboutPageLocators,
)
from pages_and_related_files.main_page import MainPage

class TestCase1():

    def test_open_link(self, browser):
        page = MainPage(
            browser,
            MainPageLocators.MAIN_LINK
        )
        page.open_site()
        page.go_to_contacts()
        contacts_page = ContactsPage(browser, browser.current_url)
        contacts_page.click_banner_tenzor()
        contacts_page.change_win()

    def test_tenzpage_link(self, browser):
        page = TenzPage(browser, TenzPageLocators.TENZ_LINK)
        page.open_site()
        time.sleep(4)

        page.banner_silavludah()
        page.about_in_block()
        page.change_win()

        page = AboutPage(browser, browser.current_url)
        page.url_about_is_right()

    def test_pic_size(self, browser):
        page = AboutPage(browser, AboutPageLocators.ABOUT_LINK)
        page.open_site()
        page.search_working_block()
        page.pictures_have_same_sizes()

