import unittest
import time
import os
import HTMLTestRunner
from common.configEmail import ConfigEmail



now_dir =os.path.dirname(os.path.abspath(__file__))

test_dir = now_dir + '\\'+'testcase'

test_report = now_dir + '\\'+'report'

print('************now_dir:',now_dir)

print('************test_dir:',test_dir)


def run_case():

    discover = unittest.defaultTestLoader.discover(test_dir,pattern="*Test.py",top_level_dir=None)
    return  discover

def clear_report():
    nowPath = os.path.dirname(__file__)
    print('nowpath',nowPath)
    reportPath = nowPath + "/" + "report"
    fileList = os.listdir(reportPath)
    #如果该目录下的文件超过5个，则开始清理
    if len(fileList)>5:
        for i in fileList:
            file = reportPath + "/" + i
            os.remove(file)

    fileNewList = os.listdir(reportPath)
    print(fileNewList)


if __name__ == '__main__':
    clear_report()
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_path = os.getcwd() + "\\report\\" + current_time + '.html'  # 生成测试报告的路径
    print(report_path)
    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"自动化测试报告", description=u'xx公司接口',verbosity=2)
    runner.run(run_case())
    fp.close()

c = ConfigEmail()
c.send_mail()

