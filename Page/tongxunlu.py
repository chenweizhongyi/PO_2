from Base.Base import Base
import Page
class TongXun(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_tianjia(self):
        # 点击添加
        self.click_element(Page.tx_tianjia)

    def click_fanhui(self):
        # 点击返回
        self.click_element(Page.tx_fanhui)

    def input_name(self,text):
        # 输入姓名
        self.input_element(Page.tx_xingming,text)

    def input_iphone(self,text):
        # 输入手机号
        self.input_element(Page.tx_dianhua,text)