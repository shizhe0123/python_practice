# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 17:20:01 2018

@author: sdc
"""

def getStringFromList(para):
    
    reStr = ''
    
    for i in range(len(para) - 1):
        reStr += str(para[i]) + ', '
    
    reStr += 'and ' 
    reStr += str(para[-1])
    
    return reStr
    