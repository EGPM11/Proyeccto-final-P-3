from pages.base_page import BasePage

class ResponsivePage(BasePage):
    def __init__(self, driver, wait):
        self.url = "url_de_tu_pagina_web"
        super().__init__(driver, wait)

    def go_to_page(self):
        super().go_to_page(self.url)

    def check_responsive(self):
        self.driver.maximize_window()
        width = self.driver.get_window_size()["width"]
        return width <= 768  # Devuelve True si es responsivo para dispositivos móviles
