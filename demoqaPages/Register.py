from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from demoqaPages.BasePage import BasePage
from demoqaConfig.ReadConfig import ReadConfig as RC
from selenium.webdriver.common.by import By
from demoqaUtilis.TestDataRead import TestDataRead as Testdata
from ddt import data, unpack

""" This class is for actions of Register page
"""

class Register(BasePage):

    textbox_firstname_id = (By.ID, "firstname")
    textbox_lastname_id = (By.ID, "lastname")
    textbox_username_id = (By.ID, "userName")
    textbox_password_id = (By.ID, "password")
    button_register_css = (By.CSS_SELECTOR, "#register")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(RC.getbaseurl()+"/register")

    """ This Function is to validate Register functionality
        1. First it will enter text in textbox of Firstnmae, lastname, username and Password
        2. Then click on Register button
        3. Captcha should be disable in QA environment
        4. Then  a. Positive Scenario - Alert with "User Register Successfully."
                 b. Negative Scenario - "User exists!"
                 c. Negative Scenario  - for password is not compliant  
        5. This function Return the Text - which can be validated as per Positive and Negative Scenario         
    """

    def do_register(self, firstname, lastname, username, password):
        self.do_send_keys(self.textbox_firstname_id, firstname)
        self.do_send_keys(self.textbox_lastname_id, lastname)
        self.do_send_keys(self.textbox_username_id, username)
        self.do_send_keys(self.textbox_password_id, password)
        self.do_action_click(self.button_register_css)

        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = Alert(self.driver)
            return alert.text
        except EC.NoAlertPresentException:
            errormessage = self.driver.find_element(By.CSS_SELECTOR, "p#name")
            return errormessage.text
        except Exception:
            return "OtherError"


        #  "User exists!"
        #  "Passwords must have at least one non alphanumeric character, one digit ('0'-'9'), one uppercase ('A'-'Z'), one lowercase ('a'-'z'), one special character and Password must be eight characters or longer."







