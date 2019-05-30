from Page.Search import Search
from Page.tongxunlu import TongXun
class Page_Zong:
    def __init__(self,driver):
        self.driver = driver

    def search(self):
        return Search(self.driver)

    def tongxun(self):
        return TongXun(self.driver)