from .base_page import BasePage
from selenium.webdriver.common.by import By


class SbisContactsPage(BasePage):

    def home_region_text(self):
        popup_regions_link = self.browser.find_element(By.CSS_SELECTOR, ".sbis_ru-Region-Chooser .sbis_ru-Region-Chooser__text")
        return popup_regions_link.text

    def partners_header(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#city-id-2"), "Partners list not found"
        partners_city = self.browser.find_element(By.CSS_SELECTOR, "#city-id-2")
        return partners_city.text

    def open_popup_regions(self):
        popup_regions_link = self.browser.find_element(By.CSS_SELECTOR, ".sbis_ru-Region-Chooser .sbis_ru-Region-Chooser__text")
        popup_regions_link.click()
        # window_name = self.browser.window_handles[-1]
        # self.browser.switch_to.window(window_name)

    def select_region(self, region):
        assert self.is_element_present(By.CSS_SELECTOR, f".sbis_ru-link[title='{region}']"), 'Selected region link not found'
        region_link = self.browser.find_element(By.CSS_SELECTOR, f".sbis_ru-link[title='{region}']")
        region_link.click()
