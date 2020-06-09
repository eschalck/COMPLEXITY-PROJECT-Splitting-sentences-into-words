# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 21:01:37 2020

@author: PC
"""

import pandas as pd
import random as rd 

def load_dictionary(file):
    """
    Reads a dictionnary. 

    Input :
        - doc : name of the text file (string, ending with .txt). 

    Returns a list containing the words of the dictionary. 
    """
    data = pd.read_csv(file, sep=" ", header=None)
    data.columns = ["word", "frequency", "pos"]
    dictionary=data['word'].tolist()
    #f=open(file,"r", encoding="utf8")
    #dictionary=f.readlines()
    for i in range(len(dictionary)):
        #takes the lines which are not empty
        if len(dictionary[i])!=0:
            dictionary[i] = dictionary[i].split(" ")[0]
    return dictionary

def quicksort(L):
    """
    Reads a dictionnary. 

    Input :
        - doc : name of the text file (string, ending with .txt). 

    Returns a list containing the words of the dictionary. 
    """
    if len(L)==0: 
        return L
    
    #choix du pivot
    pivot = L[rd.choice(range(0, len(L)))]
    
    head = quicksort([elem for elem in L if elem < pivot])
    tail = quicksort([elem for elem in L if elem > pivot])
    return head + [elem for elem in L if elem == pivot] + tail