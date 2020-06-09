# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 21:53:13 2020

@author: PC
"""
import time

def remove_punctuation(string):
    """
    Function to remove punctuations
    :param string: a string with punctuations
    :return: the string without punctuations
    """
    # punctuation marks
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~，。、'''
    for x in string:
        if x in punctuations:
            string = string.replace(x, " ")
    return string

def timer(function):
    total=0
    for k in range(5):
        start = time.clock() 
        function
        end = time.clock()
        total=total+(end-start)
    return total/5

def test_duplicate(res):
    """
    Tests if there is a duplicate in the input list. 

    Input :
        - res : result of the cut (list of strings). 

    Returns a list containing the duplicated elements. 
    """
    L_doublon=[]
    for i in range(len(res)):
        for j in range(i+1,len(res)):
            if res[i]==res[j]:
                L_doublon=L_doublon+[res[i]]
    return L_doublon