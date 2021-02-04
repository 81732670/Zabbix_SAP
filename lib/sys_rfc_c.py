#!/usr/bin/python3.8
# author:stanley
# date:2021.1.13
# 调用rfc功能模块

import pyrfc
from pyrfc import Connection
from lib.import_file import ConfigFile
from lib.show_result  import Show_Formatter

class AbapRfc:
    def __init__(self,router):
        self.imp = ConfigFile(router)
        #ssh parameter
        self.ahost    = self.imp.parameter('RFC-CONFIG', 'ashost')
        self.sysnr    = self.imp.parameter('RFC-CONFIG', 'sysnr')
        self.client   = self.imp.parameter('RFC-CONFIG', 'client')
        self.user     = self.imp.parameter('RFC-CONFIG', 'user')
        self.password = self.imp.parameter('RFC-CONFIG', 'password')

    def rfc_connect(self):
        try:
            self.conn = Connection(ashost=self.ahost,sysnr=self.sysnr, client=self.client, user=self.user, passwd=self.password)
        except Exception as e:
            print('call rfc failure!')


    # run command action  
    def run(self, rfc, title,fix_format,command_arg,output):
        if rfc == 'ENQUE_REPORT':
            result = self.conn.call(rfc,GCLIENT='',GUNAME='')
        else:
            result = self.conn.call(rfc)
        Show_Formatter(fix_format, result, title,command_arg,output)