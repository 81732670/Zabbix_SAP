#!/usr/bin/python3.8
# author:stanley
# date:2021.1.13
# 调用ssh功能模块
import re
import numpy
import paramiko
from string      import digits
from lib.import_file  import ConfigFile
from lib.show_result  import Show_Formatter

class LinuxOrder:
    def __init__(self, router):
        self.imp = ConfigFile(router)
        #ssh parameter
        self.ip = self.imp.parameter('SSH-CONFIG', 'ip')
        self.port = self.imp.parameter('SSH-CONFIG', 'port')
        self.username = self.imp.parameter('SSH-CONFIG', 'user')
        self.password = self.imp.parameter('SSH-CONFIG', 'passwd')
        self.timeout = int(self.imp.parameter('SSH-CONFIG', 'timeout'))
        self.command_arg = ''
        self.output = ''

    # run command action  
    def run(self, order, title,fix_format,command_arg,output):
        stdin, stdout, stderr = self.ssh.exec_command(order)
        Show_Formatter(fix_format, stdout, title,command_arg,output)
        
    # close ssh method
    def close_ssh(self):
        self.ssh.close()

    # connection method
    def ssh_connect(self):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(self.ip, self.port, self.username, self.password, timeout=self.timeout)
        except Exception as e:
            print('{0}：Connection Fail'.format(self.ip))
            raise e
            