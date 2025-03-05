'''Класс реализации POM для страницы pages'''

from .base_page import BasePage
from .locators import TenzPageLocators
import time

class TenzPage(BasePage):

    def banner_silavludah(self):
        #assert self.element_present(*TenzPageLocators.LOCATOR_SILAVLUDAH_BLOCK), 'Блок "Сила в людях" отсутствует'
        baner = self.browser.find_element(*TenzPageLocators.LOCATOR_SILAVLUDAH_BLOCK_TXT)
        assert baner.text == 'Сила в людях', 'Блок "Сила в людях" отсутствует'

    def about_in_block(self):
        link = self.browser.find_element(*TenzPageLocators.LOCATOR_MORE)
        super().scroll(link)
        time.sleep(4)
        link.click()


