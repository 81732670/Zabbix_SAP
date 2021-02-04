#!/usr/bin/python3.8
# author:stanley
# date:2021.1.14
# 调用db功能模块

import pyhdb
import numpy
import datetime
from lib.import_file import ConfigFile
from lib.common  import CalendarUtils
from lib.show_result import Show_Formatter
from builtins import str


class HanaDb: 
    def __init__(self, router): 
        self.imp = ConfigFile(router)
        #ssh parameter
        self.host = self.imp.parameter('DB-CONFIG', 'host')
        self.port = self.imp.parameter('DB-CONFIG', 'port')
        self.user = self.imp.parameter('DB-CONFIG', 'user')
        self.password = self.imp.parameter('DB-CONFIG', 'password')

    def db_connect(self):
        self.connection = pyhdb.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password
        ) 
    # sql method    
    def db_sql_act(self,fix_format,title,command_arg,output):
        cursor = self.connection.cursor()
        cursor.execute(self.sql)
        if 'COUNT' in self.sql:
            result = cursor.fetchone()
        else:
            result = cursor.fetchall()
        Show_Formatter(fix_format, result, title,command_arg,output)

    # run command action                
    def run(self, item,title,fix_format,command_arg,output):
        self.sql = ''
        HanaDb.db_sql_con(self,item,command_arg)
        HanaDb.db_sql_act(self,fix_format,title,command_arg,output)

    # complete sql statement
    def db_sql_con(self, item, arg):
        '''Current date '''
        if arg == 'cur_date':
           par = CalendarUtils.delta_day()
           connect = '\'' + str(par) + '\''
           self.sql = item.format(connect)
        elif arg == 'week_start_date,week_end_date':
            output = CalendarUtils.delta_week()
            week_start_date = '\''+ output[0] + '\''
            week_end_date = CalendarUtils.offset_day(output[1],1)
            week_end_date = '\''+ week_end_date + '\''
            self.sql = item.format(week_start_date,week_end_date)
        else:
            self.sql = item

       