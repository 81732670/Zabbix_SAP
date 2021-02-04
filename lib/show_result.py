#!/usr/bin/python3.8
# author:stanley
# date:2021.1.13
# 格式化输出结果

from typing import Counter
from numpy.core.records import array
from numpy.lib.arraysetops import isin
from numpy.lib.function_base import delete
from pyhdb.exceptions import DatabaseError
from lib.common  import CalendarUtils
from builtins import str

class Show_Formatter:
    def __init__(self, fix_format, data, title,arg,output):
        self.data = data
        self.title = title
        self.fix_format = fix_format
        self.arg = arg
        self.output = output
        self.show_text()

    def show_text(self):
        if self.fix_format == 'SAP-SERVICE-STATUS':
            self.Service_Status()
        elif self.fix_format == 'SAP-DEV-INFORMATION':
            self.Sap_info()
        elif self.fix_format == 'SAP-DEV-ALERT':
            self.Sap_Alert()
        elif self.fix_format == 'SAP-DEV-BACKUP':
            self.Sap_Backup()
        elif self.fix_format == 'SAP-DEV-LOG':
            self.Sap_Log()

    #format of service status
    def Service_Status(self):
    #0.GREEN 1.RED 2.YELLOW 3.GRAY
        status = ['GREEN', 'RED', 'YELLOW', 'GRAY']
        html_fix = "<b style=\"color: {};\">Green</b>"
        index = 0
        current = ''
        for line in self.data:
            position = 0
            index += 1 
            if index == 1:
                print('<b>' + (self.title) + "</b></br>" )
            elif index > 1 and index <= 5:
                continue
            
            if index > 5:
                for status_ind in status:
                    position += 1
                    if status_ind in line:
                        current = status_ind
                        position = position - 1
                        line, sep, tail = line.partition(status_ind)
                        line = line + sep
            
                status_res = line.strip("\n") + '</br>'
                status_res = status_res.replace(current,html_fix.format(current))
                print(status_res)
    #SAP-DEV-INFORMATION
    def Sap_info(self):

        #if ENQ delete <24 hour item
        if self.output == 'ENQ':
            ind,count = 0,0
            date = CalendarUtils.delta_day()
            for chk in self.data['ENQ']:
                sap_date = chk['GTDATE']
                if int(sap_date) == int(date):
                    count +=1
                
        if type(self.data) == tuple and isinstance(self.data[0], int):
            status_quantity = {0: 'green', 1: 'orange', 2: 'red'}
            if self.data[0] == 0:
                status = status_quantity[0]
            elif self.data[0] <  100 and self.data[0] > 0:
                status = status_quantity[1]
            else:
                status = status_quantity[2]
            html_fix = "<b style=\"color: {0};\">{1}</b></br>".format(status,self.data[0])
        elif type(self.data) == dict:
            quantity = len(self.data[self.output])
            if self.output == 'ENQ':
                quantity = quantity - count
            html_fix = "<b>{0}</b></br>".format(quantity)
        
        result = self.title + html_fix +'</>'
        print(result)

    def Sap_Alert(self):
        for line in self.data:
            if 'Background' in line or 'YELLOW' in line:
                continue
            else:
                print(line)
    
    def Sap_Backup(self):
        index = 0
        week = {1:'Monday:',2:'Tuesday:',3:'Wednesday:',4:'Thursday:',5:'Friday:',6:'Saturday:',7:'Sunday:'}
        status_quantity = {'successful': 'green','failed':'red','running':'orange'}
        for line in self.data:
            index += 1
            starttime = ''
            endtime = ''
            if line[1]:
                starttime = str(line[1].year) +'-' + str(line[1].month) + '-'+ str(line[1].day) +  '  ' + str(line[1].hour) + ':'+ str(line[1].minute) + ':' + str(line[1].second)
            if line[2]:
                endtime =  str(line[2].year) +'-' + str(line[2].month) + '-'+ str(line[2].day) +  '  ' + str(line[2].hour) + ':'+ str(line[2].minute) + ':' + str(line[2].second)
            output = '<b>' + week[index] + ' Backup ID: </b>' + str(line[0]) + '   '+'<b>Start Time:</b>' + starttime + '<b>End Time:</b>' + endtime + '   ' + '<b>State:</b>' + "<b style=\"color: {0};\">{1}</b></br>".format(status_quantity[line[3]],line[3])
            print(output)
            
    def Sap_Log(self):
        status_quantity = {'successful': 'green','failed':'red','running':'orange'}
        for line in self.data:
            starttime = ''
            endtime = ''
            if line[1]:
                starttime = str(line[1].year) +'-' + str(line[1].month) + '-'+ str(line[1].day) +  '  ' + str(line[1].hour) + ':'+ str(line[1].minute) + ':' + str(line[1].second)
            if line[2]:
                endtime =  str(line[2].year) +'-' + str(line[2].month) + '-'+ str(line[2].day) +  '  ' + str(line[2].hour) + ':'+ str(line[2].minute) + ':' + str(line[2].second)
            output = '<b>Backup ID:</b>' + str(line[0]) + '   '+'<b>Start Time:</b>' + starttime + '<b>End Time:</b>' + endtime + '   ' + '<b>State:</b>' + "<b style=\"color: {0};\">{1}</b></br>".format(status_quantity[line[3]],line[3])
            print(output)