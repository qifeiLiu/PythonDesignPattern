#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11 21:08
# @File    : obersver_NoModel.py
# @Software: PyCharm

__author__ = 'qifei.liu@foxmail.com'


class Receptionist():
    '''前台类
    Attributes:
        observes: Stock观察者 list 
        status: 通知的信息
    '''
    def __init__(self):
        self.observes=[]
        self.status=''
    def attach(self,observe):
        self.observes.append(observe)
    def notify(self):
        for observe in self.observes:
            observe.update()


class StockObserve():
    '''Summary of class here
       股票关注者的类
    Attributes:
        name:  接受者名字信息
        receptionist: 接收者对象
    '''
    def __init__(self,name,receptionist):
        """ Init  StockObserve"""
        self.name= name
        self.receptionist=receptionist
    def update(self):
        '''更新通知的信息
        :return: None 
        '''
        print('%s,%s停止看股票'%(self.receptionist.status,self.name))

if __name__ =='__main__':
    receptionist =Receptionist()
    observe1=StockObserve('张三',receptionist)#实例化一个观察者并传入 前台的对象
    observe2=StockObserve('李四',receptionist)
    receptionist.attach(observe1)#把股票观察者加入到通知列表里面
    receptionist.attach(observe2)

    receptionist.status = 'Boss is coming'
    receptionist.notify()

## 两个类之间的耦合性非常大
#一方面是前台类的notify 方法会调用股票观察者类的update
#当需求变动时，例如 现在老板也可以是通知者，员工除了看股票，还会看NBA
