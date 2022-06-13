from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Actions:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 3)

    def _verify_link_presence(self, link_text):
        try:
            return WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
        except TimeoutException:
            raise AssertionError("Cant find element by link text: {}".format(link_text))

    def _verify_element_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def _element(self, locator: tuple):
        return self._verify_element_presence(locator)

    def _click(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    def _send_keys(self, locator: tuple, text: str):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def _get_attrs(self, locator):
        return self.browser.execute_script(
            'var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) '
            '{ items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;',
            self._element(locator))
