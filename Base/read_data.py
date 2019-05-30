import os
import yaml
class read_data:
    def __init__(self,file_name):
        '''
                使用pytest运行在项目的根目录下运行，即PO_2目录
                期望路径为：项目所在目录/PO_2/Data/file_name
        '''
        self.file_path = os.getcwd() + os.sep + "Data" + os.sep + file_name
    def read(self):
        with open(self.file_path,'r',encoding="utf-8") as f:
            data = yaml.load(f,Loader=yaml.FullLoader)
            # print(data)
        return data
# def read():
#         with open("G:\PO_2\Data\search_data.yaml",'r',encoding="utf-8") as f:
#             data = yaml.load(f,Loader=yaml.FullLoader)
#             print(data)
# read()