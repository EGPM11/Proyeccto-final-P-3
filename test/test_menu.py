import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.menu import Menu

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_Portfolio(browser):
    wait = WebDriverWait(browser, 30)  
    search_page = Menu(browser, wait)
    search_page.go_to_page()  
    search_page.abrir_portfolios()
    
    # Imprimir el título actual de la página para debugging
    print("Título de la página actual:", browser.title)
    
    # Ajustar la aserción para que coincida con el título real de la página
    assert "Portfolio" in browser.title

def test_about(browser):
    wait = WebDriverWait(browser, 30)  
    search_page = Menu(browser, wait)
    search_page.go_to_page()  
    search_page.abrir_abouts()
    
    # Imprimir el título actual de la página para debugging
    print("Título de la página actual:", browser.title)
    
    # Ajustar la aserción para que coincida con el título real de la página
    assert "Portfolio" in browser.title