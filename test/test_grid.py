import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.grid import Grid

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_abrir_grid(browser):
    wait = WebDriverWait(browser, 30)  
    grid_page = Grid(browser, wait)
    grid_page.go_to_page()  

    grid_page.abrir_grid1()
    grid_page.abrir_grid2()
 

    # Imprimir el título actual de la página para debugging
    print("Título de la página actual:", browser.title)
    
    # Ajustar la aserción para que coincida con el título real de la página
    assert "Portfolio" in browser.title