#!/usr/bin/python3.8
# author:stanley
# date:2021.1.14
# 标准函数
import datetime
from datetime import datetime
from datetime import timedelta

#delete
class Common:
    def __init__(self,act):
        self.act = act
        
    def r_date(self,format):
        date = datetime.date.today().strftime(format)
        return date
    
    
class CalendarUtils:
    @staticmethod
    def delta_day(delta=0):
        return (datetime.now() + timedelta(days=delta)).strftime('%Y%m%d')

    @staticmethod
    def delta_week(delta=0):
        now = datetime.now()
        week = now.weekday()
        _from = (now - timedelta(days=week - 7 * delta)).strftime('%Y%m%d')
        _to = (now + timedelta(days=6 - week + 7 * delta)).strftime('%Y%m%d')
        return _from, _to

    @staticmethod
    def delta_month(delta=0):
        '''test'''
    def _delta_month(__year, __month, __delta):
        _month = __month + __delta
        if _month < 1:
            delta_year = math.ceil(abs(_month) / 12)
            delta_year = delta_year if delta_year else 1
            __year -= delta_year
            _month = delta_year * 12 + __month + __delta
        elif _month > 12:
            delta_year = math.floor(_month / 12)
            __year += delta_year
            _month %= 12
            return __year, _month
        now = datetime.now()
        _from = datetime(*_delta_month(now.year, now.month, delta), 1)
        _to = datetime(*_delta_month(_from.year, _from.month, 1), 1) - timedelta(days=1)
        return _from.strftime('%Y%m%d'), _to.strftime('%Y%m%d')

    @staticmethod
    def delta_year(delta=0):
        now = datetime.now()
        _from = datetime(now.year + delta, 1, 1)
        _to = datetime(_from.year + 1, 1, 1) - timedelta(days=1)
        return _from.strftime('%Y%m%d'), _to.strftime('%Y%m%d')

    def offset_day(date,delta):
        dateTime_p = datetime.strptime(date,'%Y%m%d').date()
        return (dateTime_p + timedelta(days=delta)).strftime('%Y%m%d')

