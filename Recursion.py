# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 11:26:00 2018

@author: Marcin
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    l = len(aStr)
    
    if l == 0:
        return False
    else:
        middle = aStr[int(l//2)]        
        if l == 1 and char != middle:
            return False
        else:
            if char == middle:
                return True
            else:
                if middle > char:
                    return isIn(char,aStr[:len(aStr)//2])
                elif middle < char:
                    return isIn(char,aStr[len(aStr)//2:])