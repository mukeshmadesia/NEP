import pytest
import os
import csv


class TestDataRead:

   
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

