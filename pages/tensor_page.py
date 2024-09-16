from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TensorPage:
    FORCE_BLOCK = (By.XPATH, "//*[contains(text(), 'Сила в людях')]")
    DETAILS_BUTTON = (By.XPATH, "//div[@class='tensor_ru-Index__block4-content tensor_ru-Index__card']//a")
    IMAGE_ITEMS = (By.CLASS_NAME, "new_lazy loaded")

    def __init__(self, driver):
        self.driver = driver

    def verify_force_block_exists(self):
        return self.driver.find_element(*self.FORCE_BLOCK).is_displayed()

    def click_details_button(self):
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*self.DETAILS_BUTTON))
       
    def verify_work_section_images(self):
        images = self.driver.find_elements(*self.IMAGE_ITEMS)
        sizes = [(img.size['height'], img.size['width']) for img in images]
        return len(set(sizes)) == 2
