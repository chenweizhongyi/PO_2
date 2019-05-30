"""
搜索
"""
from selenium.webdriver.common.by import By
# 搜索
s_1 = (By.ID,'com.android.settings:id/search')
# 搜索框
s_2 = (By.ID,'android:id/search_src_text')
# 返回箭头
s_3 = (By.CLASS_NAME,'android.widget.ImageButton')

"""
通讯录
"""
# 左上角通讯录
tx_tongxunlv = (By.XPATH,"//*[contains(@text,'通讯录')]")
# 添加按钮
tx_tianjia = (By.XPATH,"//*[contains(@content-desc,'添加新联系人')]")
# 通讯录返回按钮
tx_fanhui = (By.XPATH,"//*[contains(@content-desc,'向上导航')]")
# 姓名输入框
tx_xingming = (By.XPATH,"//*[contains(@text,'姓名')]")
# 电话输入框
tx_dianhua = (By.XPATH,"//*[contains(@text,'电话')]")
#新增联系人
tx_xinzeng = (By.XPATH,"//*[contains(@text,'新增联系人')]")

tx_nun = (By.XPATH,"//*[contains(@text,'添加电话号码')]")
# 名片名称
tx_ming = (By.ID,"com.android.contacts:id/large_title")
# 添加手机号成功
tx_nun_2 = (By.ID,"com.android.contacts:id/header")





