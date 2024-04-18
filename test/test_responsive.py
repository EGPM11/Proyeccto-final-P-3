import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.responsive import ResponsivePage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_responsive_design(browser):
    wait = WebDriverWait(browser, 30)  
    page = ResponsivePage(browser, wait)
    page.go_to_page()  

    is_responsive = page.check_responsive()

    assert is_responsive, "El diseño no es responsivo para dispositivos móviles."
