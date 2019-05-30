import os,sys
sys.path.append(os.getcwd())
from Base.read_data import read_data
import pytest
from Base.InIt_Driver import init_driver
from Page.Page_zong import Page_Zong
from Base.Base import Base
import Page
import allure

def tongxun_name_data():
    data_list = []
    read = read_data("tongxun_name_iphone.yaml").read()
    for i in read.get("name").keys():
        data_list.append(read.get("name").get(i).get("input"))
    return data_list

def tongxun_iphone_data():
    data_list = []
    read = read_data("tongxun_name_iphone.yaml").read()
    for i in read.get("iphone").keys():
        data_list.append(read.get("iphone").get(i).get("input"))
    return data_list

def tongxun_name_iphone_data():
    data_list = []
    read = read_data("tongxun_name_iphone.yaml").read()
    for i in read.get("name_iphone").keys():
        # print((read.get("name_iphone").get(i).get("name"),read.get("name_iphone").get(i).get("iphone")))
        data_list.append((read.get("name_iphone").get(i)
                          .get("name"),read.get("name_iphone").get(i).get("iphone")))
    # print(data_list)
    return data_list
# tongxun_name_iphone_data()
class Test_tongxun:

    def setup_class(self):
        self.driver = init_driver()
        self.tongxun_obj = Page_Zong(self.driver).tongxun()
        self.base_obj = Base(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture()
    def input_name_iphone(self):
        self.tongxun_obj.click_tianjia()
        self.tongxun_obj.input_name('chenwie')
        self.tongxun_obj.input_iphone('15207189874')

    @pytest.mark.run(order=1)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.issue('https:/www.baidu.com/')
    @allure.testcase('https:/www.baidu.com/xixi21')
    @allure.title('测试添加返回')
    def test_tongxun_001(self):
        self.tongxun_obj.click_tianjia()
        allure.attach('点击添加')
        assert self.base_obj.find_element(Page.tx_xinzeng),"进入添加失败"
        self.tongxun_obj.click_fanhui()
        allure.attach('点击返回')

    # @pytest.mark.run(order=2)
    # # @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    # # @allure.issue('https:/www.baidu.com/')
    # # @pytest.allure.testcase('https:/www.baidu.com/')
    # # @allure.step(title="测试步骤002")
    # def test_tongxun_002(self,input_name_iphone):
    #     self.tongxun_obj.click_fanhui()
    #     self.base_obj.keyevent(4)
    #     assert self.base_obj.find_element(Page.tx_tongxunlv)
    #
    # @pytest.mark.run(order=3)
    # # @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    # # @allure.issue('https:/www.baidu.com/')
    # # @pytest.allure.testcase('https:/www.baidu.com/youxiu')
    # # @allure.step(title="测试步骤003")
    # def test_tongxun_003(self,input_name_iphone):
    #     self.base_obj.keyevent(4)
    #     self.base_obj.keyevent(4)
    #     assert self.base_obj.find_element(Page.tx_tongxunlv)
    #
    # @pytest.mark.run(order=4)
    # @pytest.mark.parametrize("input",tongxun_name_data())
    # @allure.setp(title="测试步骤003")
    # def test_tongxun_004(self,input):
    #     self.tongxun_obj.click_tianjia()
    #     self.tongxun_obj.input_name(input)
    #     self.tongxun_obj.click_fanhui()
    #     # print(self.base_obj.find_element(Page.tx_ming).text,input)
    #     assert self.base_obj.find_element(Page.tx_ming).text == input
    #     assert self.base_obj.find_element(Page.tx_nun)
    #     self.base_obj.keyevent(4)
    # #
    # @pytest.mark.run(order=5)
    # @pytest.mark.parametrize("input",tongxun_iphone_data())
    # def test_tongxun_005(self,input):
    #     self.tongxun_obj.click_tianjia()
    #     self.tongxun_obj.input_iphone(input)
    #     self.tongxun_obj.click_fanhui()
    #     # print(self.base_obj.find_element(Page.tx_ming).text,input)
    #     # 去掉字符串中间的空格来对比
    #     assert self.base_obj.find_element(Page.tx_ming).text.replace(' ','') == input
    #     assert self.base_obj.find_element(Page.tx_nun_2).text.replace(' ','') == input
    #     self.base_obj.keyevent(4)
    #
    # @pytest.mark.run(order=6)
    # @pytest.mark.parametrize("name,iphone",tongxun_name_iphone_data())
    # def test_tongxun_006(self,name,iphone):
    #     self.tongxun_obj.click_tianjia()
    #     self.tongxun_obj.input_name(name)
    #     self.tongxun_obj.input_iphone(iphone)
    #     self.tongxun_obj.click_fanhui()
    #     # print(self.base_obj.find_element(Page.tx_ming).text,name,iphone)
    #     # 去掉字符串中间的空格来对比
    #     assert self.base_obj.find_element(Page.tx_ming).text.replace(' ', '') == name
    #     assert self.base_obj.find_element(Page.tx_nun_2).text.replace(' ', '') == iphone
    #     self.base_obj.keyevent(4)

        # if input.strip() == '':
        #     assert self.base_obj.find_element(Page.tx_nun).text == iphone
        # elif input.strip() == '':
        #     assert self.base_obj.find_element(Page.tx_nun)
        # self.driver.keyevent(4)