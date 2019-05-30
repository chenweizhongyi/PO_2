from Base.Base import Base
import Page
class Search(Base):
    def __init__(self,driver):
        # 初始化
        Base.__init__(self,driver)
    def click_ss(self):
        # 点击搜索
        self.click_element(Page.s_1)
    def input_ss(self,text):
        # 输入内容
        self.input_element(Page.s_2,text)
    def click_fh(self):
        # 点击返回
        self.click_element(Page.s_3)