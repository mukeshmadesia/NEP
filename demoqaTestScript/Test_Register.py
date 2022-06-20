from demoqaConfig.ReadConfig import ReadConfig as RC
from demoqaTests.BaseTest import BaseTest
from demoqaUtilis.TestDataRead import TestDataRead as td
import pytest
from ddt import data, unpack

class Test_Register(BaseTest):

    # username, password = td.test_data_read()
    # firstname, lastname = td.test_name_read()

    def test_RegisterPageTitle(self):

        reg = self.Register(self.driver)
        registertitle = self.reg.get_title(RC.getTitle())

        if registertitle == RC.getTitle():
            assert True
        else:
            assert False

    @data(*td.read_data_from_csv("../demoqaTestData/testdata.csv"))
    @unpack
    def test_user_registration(self, firstname, lastname, username, password):

        reg = self.Register(self.driver)
        text = self.reg.do_register(firstname, lastname, username, password)

        assert text == "User Register Successfully."





