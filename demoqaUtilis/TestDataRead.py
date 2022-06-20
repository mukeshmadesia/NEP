import pytest
import os
import csv


class TestDataRead:

    @pytest.mark.skip    # Otherwise, pytest will consider it as Testcase
    @staticmethod
    def test_data_read():
        path = '../demoqaTestData/testData.csv'

        os.chdir(os.path.abspath(os.path.dirname(__file__)))
        # home_path = Path('../Config')

        f = open("../demoqaTestData/testData.csv", "r")
        data = f.read(100)

        test_username = data.split(";")[0]
        test_password = data.split(";")[1]

        f.close()
        return test_username, test_password

    @pytest.mark.skip  # Otherwise, pytest will consider it as Testcase
    @staticmethod
    def test_name_read():
        path = '../demoqaTestData/testData.csv'

        os.chdir(os.path.abspath(os.path.dirname(__file__)))
        # home_path = Path('../Config')

        f = open("../demoqaTestData/testData.csv", "r")
        data = f.read(100)

        test_firstname = data.split(";")[2]
        test_lastname = data.split(";")[3]
        f.close()
        return test_firstname, test_lastname

    @pytest.mark.skip  # Otherwise, pytest will consider it as Testcase
    @staticmethod
    def test_searchtext_read():
        path = '../demoqaTestData/testData.csv'

        os.chdir(os.path.abspath(os.path.dirname(__file__)))
        # home_path = Path('../Config')

        f = open("../demoqaTestData/testData.csv", "r")
        data = f.read(100)

        test_searchtext = data.split(";")[4]

        f.close()
        return test_searchtext

    @pytest.mark.skip           # Otherwise, pytest will consider it as Testcase
    def test_data_write(self, outdata):
        path = '../demoqaTests/outData.txt'

        os.chdir(os.path.abspath(os.path.dirname(__file__)))
        # home_path = Path('../Config')

        f = open("outData.txt", "w")
        data = f.write("name:" + outdata)
        f.close()

    def read_data_from_csv(self, filename):
        # Create an empty List
        datalist = []

        # Open a csv file
        csvdata = open(filename, "r")

        # CSV Reader
        reader = csv.reader(csvdata)

        # skip header
        next(reader)

        # ADD csv rows to list
        for rows in reader:
            datalist.append(rows)

        return datalist

