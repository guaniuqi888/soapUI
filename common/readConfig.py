#coding=utf-8

import os
import codecs
import configparser
#获取文件的真实路径，然后分割路径和文件名存入一个元组
proDir=os.path.split(os.path.realpath(__file__))[0]
#获取上层目录
parDir=os.path.dirname(proDir)
configPath=os.path.join(parDir,"config.ini")


class ReadConfig():
    def __init__(self):
        #--实例化configparser对象
        self.cf=configparser.ConfigParser()
        #--调用read方法读取该文件（传参：文件路径和编码格式）
        self.cf.read(configPath,encoding="utf-8-sig")
    #获取配置文件中的分组（eg：Email）中的对应选项（eg：name）的值
    def get_email(self,name):
        #获取某某section下的value，name相当于key
        value=self.cf.get("EMAIL",name)
        return value
    def get_http(self,name):
        #获取某某section下的value，name相当于key
        value=self.cf.get("HTTP",name)
        return value
    def get_db(self,name):
        #获取某某section下的value，name相当于key
        value=self.cf.get("DATABASE",name)
        return value

# 测试类用
# p = ReadConfig()
# print(p.get_email('mail_host'))