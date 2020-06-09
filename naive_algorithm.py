# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 10:55:06 2020

@author: PC
"""
import list_dictionary as ld
import utility_functions as uf
import time
import matplotlib.pyplot as plt

def contains(L,element):
    """
    Checks if an element is in the list L.
    
    Cuts the sentence in words of the dictonnary and returns all possible cuts. 

    Input :
        - L : ordered dictionary (list of strings).
        - element : word to search in the dictionary (string).

    Returns a boolean. 
    """
    a = 0
    b = len(L)-1
    m = (a+b)//2
    while a < b :
        if L[m] == element or L[a]==element or L[b]==element:
            return True
        elif L[m] > element :
            b = m-1
        else :
            a = m+1
        m = (a+b)//2
    return False

def cut_1(sentence, dictionary, branch=[]):
    """
    FIRST ALGORITHM : Intuitive recursive implementation.
    
    Cuts the sentence in words of the dictonnary and returns all possible cuts. 

    Input :
        - sentence : sentence to cut (string).
        - dictionary : dictionary (list of strings). 
        - branch : cut in progress (list of strings).

    Returns all possible cuts (list of lists of strings) 
    """
    
    result=[]
    
    for i in range(1, len(sentence)+1):
        if contains(dictionary,sentence[0:i])==True:
            new_branch=branch+[sentence[0:i]]
            if i==len(sentence):
                result=result+[new_branch]
            if sentence[i+1:]!=[]:
                new_result=cut_1(sentence[i:],dictionary,new_branch)
            if len(new_result)!=0:
                result=result+new_result
                
    return result

############
#   MAIN   #
############
    
dict=ld.load_dictionary('C:/Users/PC/Documents/AGROPARISTECH 3A/COMPLEXITE/dict.txt.small.txt')
dict_sorted=ld.quicksort(dict)
time_sort_dict=uf.timer(ld.quicksort(dict))
print('time to sort the dictionary',time_sort_dict)
#time_cut=uf.timer(cut_1('汉字是构成中文文字的语素单位',dict_sorted))
#print('time to cut the sentence',time_cut)
#result=cut_1('汉字是构成中文文字的语素单位',dict_sorted)
#print(result)
#print(len(result),'different possibilities')

sentence = "汉语不同分支不一定能互通，不过不同汉语分支的人一般通晓标准官话，" \
           "各地官话标准包括中华人民共和国普通话、新马华语和中华民国国语大致相同，仅有个别字词的读音有些微分别。" \
           "书面通用语通常指现代官话白话文。大中华地区的中小学多有中国语文科，教授中文字、汉语语法、文学，又称语文课、" \
           "中文堂、国文课、华语课。在中国大陆，汉语标准为普通话以北京话为标准语音、以官话白话文著作作为语法规范，" \
           "并以此教授语文课。在香港和澳门，以粤语为通用口语及教学语言，学校会以粤语授课，但公文书面语以官话白话文为准，" \
           "亦偶有夹杂文言。在台湾及马新地区，则分别采用国语和华语为标准，并以此授中文课。此外，" \
           "中华民国、香港和澳门以繁体中文为主要文字，中华人民共和国、马来西亚及新加坡以简体中文为主要文字。" \
           "若视汉语为单一语言，汉语则为当今世界上作为母语使用人数最多的语言。世界上大约有五分之一人口以汉语为母语，" \
           "主要集中在中国大陆。海外华人亦使用汉语。在中华人民共和国、香港、澳门、中华民国及新加坡，汉语被列为官方语言，" \
           "更是联合国的正式语文和工作语言。随着大中华地区在世界的影响力增加，在一些国家逐渐兴起学习汉语的风潮。" \
           "而在部分国家为吸引华裔观光客，会在主要车站、机场等公共场所及观光地区增加中文的标示及说明，" \
           "部分服务业亦会安排通晓汉语的服务人员。"

text=uf.remove_punctuation(sentence).split(' ')

start = time.clock() 
res_list=[]
for sub_text in text:
    if len(sub_text)>0:
        r=cut_1(sub_text,dict_sorted)
        res_list=res_list+[r]
end = time.clock()
print('time to cut the sentence',end-start)

"""

#study of the complexity in time : variation of the length of the sentence. 
sentence2 = ''.join(text)
sentence2 = sentence2[0:40]

x1=range(0,len(sentence2))
y1=[0 for j in range(0,len(sentence2))]
for i in range(5):
    print(i)
    for k in range(1,len(sentence2)):
        start = time.clock() 
        cut_1(sentence2[0:k],dict_sorted)
        end = time.clock()
        y1[k]=y1[k]+(end-start)
y1=[x/5 for x in y1]

plt.plot(x1,y1)
plt.xlabel('Lenght of the sentence (nb of characters)')
plt.ylabel('Time (second)')
plt.show()
"""
