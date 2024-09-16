import time
from selenium.webdriver.common.by import By

class SBISPage:
    CONTACTS_LINK = (By.LINK_TEXT, 'Контакты')
    TENSOR_BANNER = (By.XPATH, "//a[contains(@title, 'tensor.ru')]")
    REGION_DROPDOWN = (By.XPATH, "//span[@class='sbis_ru-Region-Chooser ml-16 ml-xm-0']/span")
    PARTNERS_LIST = (By.CLASS_NAME, "controls-ListView__itemV-relative")

    def __init__(self, driver):
        self.driver = driver

    def go_to_contacts(self):
        self.driver.find_element(*self.CONTACTS_LINK).click()

    def click_tensor_banner(self):
        self.driver.find_element(*self.TENSOR_BANNER).click()

    def current_region(self):
        return self.driver.find_element(*self.REGION_DROPDOWN).text
    
    def get_partner_list(self):
        partners = self.driver.find_elements(*self.PARTNERS_LIST)
        return len(partners)

    def select_region(self, region_name):
        self.driver.find_element(*self.REGION_DROPDOWN).click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, f"[title='{region_name}']").click()
        time.sleep(2)

    def current_title(self):
        return self.driver.title

