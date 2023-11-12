# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 21:38:00 2023

@author: Mario
"""
import interfaz

class op ():
    def __init__(self):
        self._n1=0
        self._n2=0
    
    @property
    def n1(self):
        return self._n1
    
    @property
    def n2(self):
        return self._n2
    
    @n1.setter
    def  n1 (self, num1):
        self._n1=num1
        
    @n2.setter
    def  n2 (self, num2):
        self._n2=num2
        
    def sumar(self):
        