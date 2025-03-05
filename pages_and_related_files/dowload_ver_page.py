'''Класс реализации POM для страницы загрузки'''

import time
import re
import os

from .base_page import BasePage
from .locators import DownloadSabyLocators

class DownloadFiles(BasePage):

    def size_web_file_info(self):
        button4 = self.browser.find_element(*DownloadSabyLocators.LOCATOR_DOWLOAD_HREF_BUTTON)
        buttontxt = "".join(re.findall("\d+\.+\d+", button4.text))
        buttonfloat = float(buttontxt)
        time.sleep(2)

        path_file_dir = os.path.dirname(os.path.abspath(__file__))
        path_file_dir_all = path_file_dir + "\sbisplugin-setup-web.exe"

        super().check_dowload_end(path_file_dir)
        file_info = os.stat(path_file_dir_all)
        file_size = file_info.st_size
        file_size = float(file_size / 1048576)
        file_size = round(file_size, 2)
        print(file_size)
        print(buttonfloat)
        assert  file_size==buttonfloat, 'размер файла не совпадает с указанным на сайте'
        time.sleep(5)

        os.remove(path_file_dir_all) #удаляем файл




