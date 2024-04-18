from pages.base_page import BasePage
from Data.locators import menulocators
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By


class Menu(BasePage):
    def __init__(self, driver, wait):
        self.url = "C:\Users\18496\OneDrive\Escritorio\Final\index.html"
        self.locator = menulocators
        super().__init__(driver, wait)

    def go_to_page(self):
        super().go_to_page(self.url)

    def abrir_portfolio(self): 
        self.driver.find_element(*self.locator.portfolio).click()

        self.driver.save_screenshot("results/foto_portfolios.png")

    def abrir_about(self): 
        self.driver.find_element(*self.locator.about).click()

        self.driver.save_screenshot("results/foto_abouts.png")
        