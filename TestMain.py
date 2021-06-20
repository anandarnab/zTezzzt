#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 00:06:18 2021

@author: anandpadhi
"""

class A:
    def __init__(self, a, b):
        self.aV = a
        self.bV = b
        
    @staticmethod 
    def statMethod(i,a):
        i ^= 5
        a *= 6
        return a//i
    
    
class B: 
    
    def __init__(self):
        print('A class B def here')
        
    
a = A()
a.statMethod(4, 24)