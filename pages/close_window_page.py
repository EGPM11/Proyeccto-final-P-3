from pages.base_page import BasePage
from Data.locators import gridlocators  # Asegúrate de importar los localizadores correctos

class CloseWindowPage(BasePage):
    def __init__(self, driver, wait):
        self.url = "url_de_tu_pagina_web"
        self.locator = gridlocators  # Usa los localizadores correspondientes
        super().__init__(driver, wait)

    def go_to_page(self):
        super().go_to_page(self.url)

    def click_close_button(self, modal_id):
        self.driver.find_element_by_id(modal_id).click()
