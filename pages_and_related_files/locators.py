'''Локатары для всех pages'''

from selenium.webdriver.common.by import By

class MainPageLocators():
    MAIN_LINK = 'https://sbis.ru/'
    LOCATOR_CONTACTS_BUTTON = (By.CSS_SELECTOR,
                               '.sbisru-Footer__list-item [href="/contacts"]')

class ContactsPageLocators():
    CONTACTS_LINK = 'https://sbis.ru/contacts/'
    LOCATOR_TENZOR_BANNER = (By.CSS_SELECTOR,
                             '.sbisru-Contacts__logo-tensor.mb-12')

class TenzPageLocators():
    TENZ_LINK = 'https://tensor.ru/'
    LOCATOR_SILAVLUDAH_BLOCK_TXT = (By.CSS_SELECTOR,
                                "#container > div.tensor_ru-content_wrapper > "
                                "div > div.tensor_ru-Index__block4-bg > "
                                "div > div > div:nth-child(1) > div > "
                                "p:nth-child(1)")
    LOCATOR_SILAVLUDAH_BLOCK = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-content'
                                                 '.tensor_ru-Index__card')
    LOCATOR_MORE = (By.CSS_SELECTOR,
                    '.tensor_ru-Index__block4-content.tensor_ru-Index__card '
                    '.tensor_ru-link')

class AboutPageLocators():
    ABOUT_LINK = 'https://tensor.ru/about'
    LOCATOR_WORKING = (By.CSS_SELECTOR,
               '.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3')
    LOCATOR_PHOTOS = (By.CSS_SELECTOR,
              '.tensor_ru-container'
              '.tensor_ru-section.tensor_ru-About__block3 img')

class RegionLocators():
    LOCATOR_REGION = (By.CSS_SELECTOR, '.sbis_ru-Region-Chooser__text'
                                       '.sbis_ru-link')
    LOCATOR_REGION_BUTTON = (By.CSS_SELECTOR, '.sbis_ru-Region-Chooser__text'
                                              '.sbis_ru-link')
    LOCATOR_REGION_PARTNERS_BLOCK = (By.CSS_SELECTOR, '[name="itemsContainer"]')
    LOCATOR_REGION_PARTNERS_NAME = (By.CSS_SELECTOR, '.sbisru-Contacts-List__name')
    LOCATOR_REGION_KAMCHATKA = (By.CSS_SELECTOR, '[title="Камчатский край"]')

class DownloadSabyLocators():

    LOCATOR_DOWNLOAD_LOCAL_VER_BUTTON = (By.CSS_SELECTOR, "#container > div.sbisru-Footer.sbisru-Footer__scheme--default > "
                                                          "div.sbis_ru-container > div.sbisru-Footer__container > "
                                                          "div:nth-child(3) > ul > li:nth-child(10) > a")
    LOCATOR_DOWLOAD_LINK_MY_VER = 'https://update.saby.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe'
    LOCATOR_DOWLOAD_HREF_BUTTON = (By.CSS_SELECTOR, ".sbis_ru-DownloadNew-loadLink__link.js-link")