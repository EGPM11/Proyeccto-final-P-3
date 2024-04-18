import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.close_window_page import CloseWindowPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_close_window_modal1_2(browser):
    wait = WebDriverWait(browser, 30)  
    page = CloseWindowPage(browser, wait)
    page.go_to_page()  

    modals = ["portfolioModal1", "portfolioModal2"]

    for modal_id in modals:
        page.click_close_button(modal_id)
        assert not browser.find_element_by_id(modal_id).is_displayed(), f"Modal {modal_id} should be closed"
