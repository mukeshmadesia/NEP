import pytest
from demoqaTests import conftest


@pytest.mark.usefixtures("init_driver")
class BaseTest:

    def __init__(self):
        print("--inside BaseTest--")
        pass
