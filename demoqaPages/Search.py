from selenium.webdriver.common.by import By
from demoqaConfig.ReadConfig import ReadConfig as RC
from demoqaPages.BasePage import BasePage


"""
This class is for search functionality of Books
"""


class SearchPage(BasePage):

    print("--inside SearchPage--")

    def __init__(self, driver):
        super().__init__(self.driver)
        self.driver.get(RC.getbaseurl() + "/books")

    """ This function is to Verify SEARCH Functionality
        1. Search Text can be Present in Book, Author or Publisher text
        2. So This functions Fist enter the given text in Search Box - Using send_keys
        3. Then This function fetches list of all books, Authors and Publisher 
        4. Then This function checks given text is present in either Book, Author or Publisher text.
        5. if text is present then function loop will keep checking - and return True
        6. if text is not present in any element of same row then function will break and return False
        7. Function will return false - if no result is found        
    """

    def do_search_book(self, searchtext):

        textbox_searchbox_id = (By.ID, "searchBox")
        self.do_send_keys(textbox_searchbox_id, searchtext)

        bookXpath = "//span//a"
        authorXpath = "//a//parent::span//..//..//following-sibling::div[@class='rt-td'][1]"
        publisherXpath = "//a//parent::span//..//..//following-sibling::div[@class='rt-td'][2]"

        l1 = self.driver.find_elements(By.XPATH, bookXpath)
        l2 = self.driver.find_elements(By.XPATH, authorXpath)
        l3 = self.driver.find_elements(By.XPATH, publisherXpath)

        flag = False  # Initialise the Flag

        if len(l1) == 0:
            return flag

        for x, y, z in zip(l1, l2, l3):

            if (searchtext.lower() in x.text.lower()) \
                    or (searchtext.lower() in y.text.lower()) \
                    or (searchtext in z.text.lower()):
                flag = True
            else:
                flag = False
                break

        return flag

