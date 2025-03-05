'''Класс с методами для работы с WebDriver'''
import os
import time
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import browser

class BasePage():

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url



    def open_site(self):
        self.browser.get(self.url)

    def change_win(self):
        new_page = self.browser.window_handles[1]
        self.browser.switch_to.window(new_page)

    def scroll(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)


    def findd_element(self, locator, time=10):
        (WebDriverWait(self.browser,time)
         .until(EC.presence_of_element_located(locator),
                message=f"Can,t find element by locator {locator}"))

    def findd_elements(self, locator, time=10):
        (WebDriverWait(self.browser,time)
         .until(EC.presence_of_all_elements_located(locator),
                message=f"Can,t find element by locator {locator}"))

    def element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    '''Проверка наличия загруженного плагина по наличию/отсутсвию временного файла'''
    def check_dowload_end(self, path_file, timeout=30):
        sec = 0

        while sec < timeout:
            files = os.listdir(path_file)
            if any(file.endswith(".crdownload") for file in files):
                time.sleep(1)
                sec += 1
            else:
                return True
        return False
