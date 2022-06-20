from demoqaConfig.ReadConfig import ReadConfig as RC
from demoqaPages.LoginPage import LoginPage
from demoqaTests.BaseTest import BaseTest
from demoqaUtilis.TestDataRead import TestDataRead as td
import pytest
from ddt import data, unpack


class Test_Login(BaseTest):

    username, password = td.test_data_read()
    print("--Inside-Testlogin--")
    print(username)
    print(password)

    def test_login_page_title(self):

        lp = LoginPage(self.driver)
        logintitle = self.lp.get_title(RC.getTitle())

        if logintitle == RC.getTitle():
            assert True
        else:
            assert False

    @data(*td.read_data_from_csv("../demoqa.TestData/testData.csv"))
    @unpack
    def test_user_login(self, username, password):
        lp = LoginPage(self.driver)
        uservalue = self.lp.do_login(username, password)
        assert uservalue == username




