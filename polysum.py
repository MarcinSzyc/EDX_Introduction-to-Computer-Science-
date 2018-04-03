# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 14:42:14 2018

@author: Marcin
"""
import math
def polysum(n,s):
    area = (0.25*n*(s*s))/(math.tan(math.pi/n))
    perim = n*s
    return round((area + math.pow(perim,2)),4)