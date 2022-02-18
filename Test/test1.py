# -*- coding: utf-8 -*-
"""
Created on Fri May 14 16:04:48 2021

@author: laoba
"""

class test1():
    x=1
    def __int__(self):
#        self.x=3
        return 

    
class test2(test1):
    def __init__(self):
        self.x=2
        return 
    
class test3(test1):
    def __init__(self):
        super(test1).__init__()
        print(self.x)
        return

A0=test1()
print(A0.x)

A=test2()
B=test3()
    
    