from pages.base_page import BasePage
from Data.locators import gridlocators

class Grid(BasePage):
    def __init__(self, driver, wait):
        self.url = "C:\Users\18496\OneDrive\Escritorio\Final\index.html"
        self.locator = gridlocators
        super().__init__(driver, wait)

    def go_to_page(self):
        super().go_to_page(self.url)

    
    def abrir_grid3(self): 
        self.driver.find_element(*self.locator.grid3).click()
        self.driver.save_screenshot("results/foto_grid3.png")

    def abrir_grid4(self): 
        self.driver.find_element(*self.locator.grid4).click()
        self.driver.save_screenshot("results/foto_grid4.png")
