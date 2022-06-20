import json
from pathlib import Path
import os

""" This class is to Read the demoQA url & Title from Json data file
    then url will be used in subsequent program
"""

# Opening JSON file
path = '../demoqaConfig/config.json'

# Open file
f = open(path)

# returns JSON object as a dictionary
data = json.load(f)


class ReadConfig:

    @staticmethod
    def getregisterurl():
        demoqa_url = data['demoqa_url']
        return demoqa_url

    @staticmethod
    def getTitle():
        demoqa_title = data['demoqa_title']
        return demoqa_title

    @staticmethod
    def getloginurl():
        demoqa_login_url = data['demoqa_login_url']
        return demoqa_login_url

    @staticmethod
    def getbaseurl():
        demoqa_base_url = data['baseurl']
        return demoqa_base_url



print(ReadConfig.getTitle())
print(ReadConfig.getregisterurl())
print(ReadConfig.getloginurl())
print(ReadConfig.getbaseurl())
