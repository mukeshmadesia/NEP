from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

""" 
As per Page Object Model - common functionality has been created in one Class
"""

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    """ This is click function - Input = locator of element"""
    def do_click(self, by_locator):

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    """ This is to Enter text in textBox - Input = text"""
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys()

    """ This is to get text of element - Input = Locator of element"""
    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    """ This is to check is element is visible or not - Input = locator"""
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element

    """ This is to get Title of URL"""
    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    """ This is click function via action class - Input = locator of element"""
    """ Some elements need action class to click"""

    def do_action_click(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        action = ActionChains(self.driver)
        action.click(on_element=element)
        action.perform()
