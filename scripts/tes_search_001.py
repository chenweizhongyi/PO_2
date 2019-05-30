import sys,os
sys.path.append(os.getcwd())
from Page.Page_zong import Page_Zong
from Base.InIt_Driver import init_driver
import pytest
from Base.read_data import read_data

def  package_param_data():
    list_data = []
    yaml_data = read_data("search_data.yaml").read()
    for i in yaml_data.keys():
        list_data.append((i,yaml_data.get(i).get("input_text")))
    return list_data

class Test_search:
    def setup_class(self):
        # 实例化driver对象
        self.driver = init_driver()
        # 同一对象管理类
        self.search_obj = Page_Zong(self.driver).search()
    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture("class")
    def click_sousuo(self):
        self.search_obj.click_ss()


    @pytest.mark.usefixtures("click_sousuo")
    @pytest.mark.parametrize("test_num,data",package_param_data())
    def test_001(self,test_num,data):
        print("运行测试用例%s"%(test_num))
        self.search_obj.input_ss(data)
        self.driver.get_screenshot_as_file('./screen/%s.png'%(test_num))
        # self.search_obj.click_fh()
