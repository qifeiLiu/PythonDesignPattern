#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11 22:02
# @File    : ObserverModel.py
# @Software: PyCharm

__author__ = 'qifei.liu@foxmail.com'

from abc import ABCMeta, abstractclassmethod


class Subject():
    __metaclass__ = ABCMeta
    observers=[]
    status=''

    @abstractclassmethod
    def attach(self,observer):
        pass
    @abstractclassmethod
    def detach(self,observer):
        pass

    @abstractclassmethod
    def notify(self):
        pass

class Observer():
    __metaclass__ = ABCMeta
    def __init__(self,name,sub):
        self.name = name
        self.sub = sub
    @abstractclassmethod
    def update(self):
        pass

class Boss(Subject):
    def __init__(self):
        pass
    def attach(self,observer):
        self.observers.append(observer)
    def detach(self,observer):
        self.observers.remove(observer)
    def notify(self):
        for observer in self.observers:
            observer.update()

class StockObserver(Observer):
    def update(self):
        print('%s,%s停止看股票'%(self.sub.status,self.name))

class NBAObserver(Observer):
    def update(self):
        print('%s,%s停止看NBA'%(self.sub.status,self.name))

if __name__=='__main__':
    boss = Boss()
    observe1 = StockObserver('张三',boss)
    observe2 = StockObserver('李四',boss)
    boss.attach(observe1)
    boss.attach(observe2)
    boss.status = '我是老板，我来了'
    boss.notify()
