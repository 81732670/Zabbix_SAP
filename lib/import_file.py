#!/usr/bin/python3.8
# author:stanley
# date:2021.1.13
# 解析配置文件

import configparser

class ConfigFile:
    def __init__(self, route):
        self.imp = configparser.ConfigParser()
        self.imp.read(route)      

    def parameter(self, type, para):
        value = self.imp.get(type,para)
        return value
    
    def command(self, type):
        list = self.imp.items(type)
        return list

    #获取配置文件下的所有key
    def get_key(self, type):
        key = self.imp.options(type)
        return key