import xlrd
import os
class readData():
    #获取当前的目录，D:/python3.8/untitled7
    path=os.path.dirname(os.path.split(os.path.abspath(__file__))[0])
    #拼接找到data.xls
    data_dir=path +'\\'+'data'+'\\'+'data.xls'


    #获取数据
    #
    def get_data(self,Method,file=data_dir):
        workbook = xlrd.open_workbook(file)
        sheet = workbook.sheet_by_index(0)
        ...
        cols1 = sheet.col_values(1)
        cols2 = sheet.col_values(2)
        test_data=[]
        for i in cols1:
            if Method == i:
                data = cols2[cols1.index(i)]
                List = data.split(',')
                test_data = List
        return test_data

# if __name__=='__main__':
#     a = readData()
#     print(a.get_data('test_Search'))
#     print(a.data_dir)
#     print(a.get_data('test_AHomeTest_Search'))









