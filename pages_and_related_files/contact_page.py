'''Класс реализации POM для страницы contacts'''

import time
from .base_page import BasePage
from .locators import ContactsPageLocators
from .locators import RegionLocators

class ContactsPage(BasePage):

    def click_banner_tenzor(self):
        link = self.browser.find_element(*ContactsPageLocators.LOCATOR_TENZOR_BANNER)
        link.click()

    def region_in_contacts(self):
        regions = self.browser.find_element(*RegionLocators.LOCATOR_REGION)
        assert regions.text == 'Костромская обл.', 'Регион не верный'

    def region_in_contacts_button(self):
        regions_button = self.browser.find_element(*RegionLocators.LOCATOR_REGION_BUTTON)
        regions_button.click()
        time.sleep(4)
        other_region = self.browser.find_element(*RegionLocators.LOCATOR_REGION_KAMCHATKA)
        other_region.click()

    def region_contacts_block(self):
        regions_partners_block = self.browser.find_element(*RegionLocators.LOCATOR_REGION_PARTNERS_BLOCK)
        assert regions_partners_block, 'Нет блока партнеров'

    def check_and_save_info_regions(self):
        region_ms = []
        name_ms = self.browser.find_element(*RegionLocators.LOCATOR_REGION)
        url_ms = self.browser.current_url
        title_ms = self.browser.title
        partners_block_ms = []
        for i in self.browser.find_elements(*RegionLocators.LOCATOR_REGION_PARTNERS_NAME):
            partners_block_ms.append(i.text)
        region_ms.append(name_ms.text)
        region_ms.append(url_ms)
        region_ms.append(title_ms)
        region_ms.append(partners_block_ms)
        return region_ms

    def check_change_region(self, old_inf, new_inf):
        for i in range(len(old_inf)):
            if i == 0:
                assert old_inf[i] != new_inf[i], 'Регион возле заголовка "контакты" не поменялся'
            elif i == 1:
                assert old_inf[i] != new_inf[i], 'URL страницы не изменился'
            elif i == 2:
                assert old_inf[i] != new_inf[i], 'title вкладки не поменялся'
            elif i == 3:
                assert old_inf[i] != new_inf[i], 'Список партнеров не поменялся'




