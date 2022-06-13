from selenium.webdriver.common.by import By
from page_objects.Actions import Actions


class BasePage(Actions):
    SEARCH_FIELD = (By.XPATH, "//input[@title='Поиск']")
    SEARCH_BUTTON = (By.XPATH, "//input[@value='Поиск в Google']")
    JOIN = (By.XPATH, "//div[@class='home-banner__col-btn']/a[text()='join our team!']")

    def send_text_to_search_field(self, text):
        self._send_keys(self.SEARCH_FIELD, text)
        self._click(self.SEARCH_BUTTON)

    def go_to_site(self, text):
        self._click((By.XPATH, f"//h3[text()='{text}']"))

    def get_join_our_team_button(self):
        return self._get_attrs(self.JOIN)
