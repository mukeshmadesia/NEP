from demoqaPages.Search import SearchPage
from demoqaTests.BaseTest import BaseTest
from demoqaUtilis.TestDataRead import TestDataRead as td
import pytest
from ddt import data, unpack


class Test_search(BaseTest):

    @data(*td.read_data_from_csv("../demoqaTestData/testdata.csv"))
    @unpack
    def test_search(self, searchtext):
        sp = SearchPage(self.driver)
        flag = sp.do_search_book(self, searchtext)

        assert flag


