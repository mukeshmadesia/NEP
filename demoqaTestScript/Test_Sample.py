import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from Tests.test_base import BaseTest
from selenium import webdriver
import allure

@allure.severity(allure.severity_level.NORMAL)
class Test_sample:

    def test_user_login(self):

        uservalue = self.lp.do_login(Test_Login.username, Test_Login.password)
        assert uservalue == Test_Login.username

    def test_register_page_title(self):
        path = "C:\\Users\\Nikky Raj\\Downloads\\Downloaded Software\\Selenium\\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=path)
        self.driver.get("https://demoqa.com/register")
        WebDriverWait(self.driver, 10).until(EC.title_is('ToolsQA'))
        title = self.driver.title
        print(title)
        assert title == 'ToolsQA'
        self.driver.close()

    def test_search_bookText(self):
        path = "C:\\Users\\Nikky Raj\\Downloads\\Downloaded Software\\Selenium\\chromedriver.exe"

        #wait = WebDriverWait(self.driver, 10)
        self.driver = webdriver.Chrome(executable_path=path)
        self.driver.get("https://demoqa.com/books")
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, "searchBox").send_keys('Git')
        locator = (By.XPATH, "//span//a")

        l1 = self.driver.find_elements(By.XPATH, "//span//a")
        print(len(l1))
        flag = False

        for e in l1:
            link_text = e.text
            if "Git" in link_text:
                flag = True

        assert flag


        # -- //a//parent::span//..//following::div[@class='rt-td']


    def test_do_register(self):
        path = "C:\\Users\\Nikky Raj\\Downloads\\Downloaded Software\\Selenium\\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=path)
        self.driver.get("https://demoqa.com/register")

        # UserName = (By.ID, "txtUsername")
        # Password = (By.ID, "txtPassword")
        # LoginBtn = (By.ID, "btnLogin")

        self.driver.find_element(By.ID, "firstname").send_keys('Mukesh')
        self.driver.find_element(By.ID, "lastname").send_keys('Madesia')
        self.driver.find_element(By.ID, "userName").send_keys('mukeshmadesia')
        self.driver.find_element(By.ID, "password").send_keys('Avi@14nov')

        action = ActionChains(self.driver)
        captcha_xpath = "//div[@class ='recaptcha-checkbox-border']"

        # // div[@class ='recaptcha-checkbox-border']
        Captha_locator = (By.XPATH, captcha_xpath)


        # captcha = self.driver.find_element(By.XPATH, "//div[@class='recaptcha-checkbox-border']")
        #
        # action.click(on_element=captcha)
        # action.perform()
        reg_locator = (By.XPATH, "//button[@id='register']")

        register = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(reg_locator))

        self.driver.switch_to_default_content()
        #register = self.driver.find_element(By.XPATH, "//button[@id='register']")

        #action = ActionChains(self.driver)
        action.click(on_element=register)
        action.perform()



        # captcha_xpath = "div[@class ='recaptcha-checkbox-border']"
        # Captha_locator = (By.XPATH, captcha_xpath)
        # print(captcha_xpath)

        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Captha_locator)).click()
        # print(element)
        #self.driver.find_element(By.XPATH, captcha_xpath).click()

        assert True


