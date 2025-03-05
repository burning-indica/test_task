'''Класс с тест-кейсом №2 (бизнес-логика)'''

import time
from pages_and_related_files.contact_page import ContactsPage
from pages_and_related_files.locators import (
    MainPageLocators, ContactsPageLocators
)
from pages_and_related_files.main_page import MainPage

class TestCase2():

    def test_open_link(self, browser):
        page = MainPage(
            browser,
            MainPageLocators.MAIN_LINK
        )
        page.open_site()
        time.sleep(2)
        page.go_to_contacts()
        contacts_page = ContactsPage(browser, browser.current_url)
        contacts_page.region_in_contacts()
        contacts_page.region_contacts_block()
        time.sleep(2)

    def test_change_region(self, browser):
        contacts_page = ContactsPage(browser, ContactsPageLocators.CONTACTS_LINK)
        contacts_page.open_site()

        old_inf = contacts_page.check_and_save_info_regions()
        contacts_page.region_in_contacts_button()

        time.sleep(5)
        new_inf = contacts_page.check_and_save_info_regions()
        contacts_page.check_change_region(old_inf, new_inf)

