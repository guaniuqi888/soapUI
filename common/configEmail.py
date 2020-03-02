# coding:utf-8

'''
功能：
    1.配置发送邮件属性
    2.读取邮件配置
    3.发送邮件
'''
import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.readConfig import ReadConfig
from email.header import Header


class ConfigEmail():
    # 读取ini文件配置属性
    r = ReadConfig()
    mail_host = r.get_email('mail_host')
    # 配置第三方SMTP服务
    mail_host1 = "smtp.126.com"  # 设置服务器
    mail_user = r.get_email('mail_user')  # 用户名

    mail_pass = r.get_email('mail_pass')  # 口令

    # 配置邮件属性
    sender = r.get_email('sender')
    receivers = r.get_email('receiver')
    content = r.get_email('content')
    msg = MIMEMultipart()

    def config_file(self):
        # 配置附件属性
        file = self.find_file()
        print(file)
        sendfile = open(file, 'rb').read()
        att = MIMEText(sendfile, 'plain', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename=report.html'
        self.msg.attach(att)
        self.msg['From'] = self.sender
        self.msg['To'] = self.receivers
        self.msg['Subject'] = Header('Python自动化测试报告', 'utf-8')
        self.msg.attach(MIMEText('这是接口自动化报告邮件，如果想查看详情请查收附件', 'plain', 'utf-8'))


    def find_file(self):
        '''查找最新文件'''
        # 获取当前路径
        current_path = os.path.dirname(os.path.abspath(__file__))
        # print('current',current_path)
        # 获取报告的存放路径
        filePath = os.path.dirname(current_path) + "/" + 'report'
        # print('filepath',filePath)

        # 获取filepath路径下全部文件名称的列表
        fileList = os.listdir(filePath)
        # print(fileList)

        fileDict = {}
        fileTime = []

        for iName in fileList:
            # 拼接文件路径和i-文件名
            filename = filePath + "/" + iName
            # 获取该文件的修改时间
            iTime = os.path.getmtime(filename)
            # 将该文件的修改时间追加到时间列表中
            fileTime.append(iTime)
            # 将文件名iname作为字典的value，文件的修改时间iTime作为字典的key存入
            fileDict[iTime] = iName
        # print(fileDict,fileTime)

        sendfilekey = max(fileTime)
        sendfile = fileDict[sendfilekey]
        # rint(sendfile)
        sendfile = filePath + "/" + sendfile

        return sendfile

        # 发送邮件

    def send_mail(self):
        self.config_file()

        s = smtplib.SMTP()

        # print(self.mail_host,self.mail_user,self.mail_pass,self.sender,self.receivers,self.message.as_string)
        s.connect(self.mail_host, 25)  # 25 为 SMTP 端口号
        # s.set_debuglevel(1)
        s.login(self.mail_user, self.mail_pass)
        s.sendmail(self.sender, self.receivers, self.msg.as_string())
        print("邮件发送成功")

# if __name__ == '__main__':
#     pass
# c = ConfigEmail()
# c.send_mail()
