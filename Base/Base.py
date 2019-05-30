from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,type,timeout=10,poll=0.5):
        """
        :param type: 输入（）参数，比如（By.ID,'io.manong.developerdaily:id/btn_login'）
        :param timeout:
        :param poll:
        :return:
        """
        # 返回元素对象
        return WebDriverWait(self.driver,timeout,poll)\
            .until(lambda x:x.find_element(*type))
    def click_element(self,type):
        # 点击操作
        el = self.find_element(type)
        el.click()

    def input_element(self,type,text):
        # 输入操作
        el = self.find_element(type)
        el.clear()
        el.send_keys(text)

    def get_png(self,text):
        """
        :param text: 文件名
        :return:
        """
        self.driver.get_screenshot_as_file('./screen/%s.png'%(text))

    def keyevent(self,num):

        self.driver.keyevent(num)