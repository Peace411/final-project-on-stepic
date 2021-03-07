from .base_page import BasePage
from selenium.webdriver.common.by import By
class MainPage(BasePage):
    def go_to_login_page(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login"), "Login link is not presented"
        