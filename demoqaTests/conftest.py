import pytest
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=['chrome', 'firefox'], scope='class')
def init_driver(request):

    if request.param == "chrome":
        # Or use executable_path to pass driver path
        # web_driver = webdriver.Chrome(ChromeDriverManager().install())

        chrome_driver_path = "C:\\Users\\Nikky Raj\\Downloads\\Downloaded Software\\Selenium\\chromedriver.exe"
        web_driver = webdriver.Chrome(executable_path=chrome_driver_path)
        print("--confit-test--")
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    request.cls.driver = web_driver

    yield
    web_driver.close()





