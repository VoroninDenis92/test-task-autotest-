import pytest
from selenium import webdriver
from pages.sbis_page import SBISPage
from pages.tensor_page import TensorPage

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_tensor_page(driver):
    sbis = SBISPage(driver)
    tensor = TensorPage(driver)

    driver.get('https://sbis.ru/')
    sbis.go_to_contacts()
    sbis.click_tensor_banner()

    driver.get('https://tensor.ru/')
    assert tensor.verify_force_block_exists()

    tensor.click_details_button()
    assert 'https://tensor.ru/about' in driver.current_url

    assert tensor.verify_work_section_images()

def test_region_change(driver):
    sbis = SBISPage(driver)
    driver.get('https://sbis.ru/')
    sbis.go_to_contacts()
    
    assert 'Нижегородская обл.' in sbis.current_region()

    assert sbis.get_partner_list() != 0
    partners_list_1 = sbis.get_partner_list()

    sbis.select_region('Камчатский край')
    assert 'Камчатский край' in sbis.current_region()
    assert sbis.get_partner_list() != partners_list_1, "Не равны"
    assert driver.current_url.startswith('https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients')
    assert "СБИС Контакты — Камчатский край" in sbis.current_title()
