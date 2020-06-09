import time
import matplotlib.pyplot as plt
import tree_dictionary as td
import utility_functions as uf
dict_chinese=td.dict_chinese

def cut_all(dict,text,dict_p=None,p=0,i=1):
    """
    a cut that give all the possibilities
    :param dict: dictionary tree
    :param text: a text without punctuations and ' '
    :param dict_p: a dictionary, keys : position pi, value : all the possible combination from the position
    :param p: a position
    :param i: length of word
    :return: dict_p: a dictionary that stocks all the possible combination from all positions
    """
    if dict_p==None:
        dict_p={}
    tree=dict.find_char(text[p:p+i])
    l_text=len(text)
    l_tree=len(tree.char)
    if p+l_tree==l_text and tree.is_word:
        if p in dict_p.keys():
            if [tree.char] not in dict_p[p]:
                dict_p[p] = dict_p[p] + [[tree.char]]
        else:
            dict_p[p]=[[tree.char]]
    else:
        if tree.is_word:
            cut_all(dict, text, dict_p, p + l_tree)
            if p+l_tree in dict_p.keys():
                cut_list = []
                for l in dict_p[p+l_tree]:
                    cut_list.append([tree.char]+l)
                if p in dict_p.keys():
                    if cut_list[0] not in dict_p[p]:
                        dict_p[p]=dict_p[p]+cut_list
                else:
                    dict_p[p] = cut_list
    if i+p<=l_text:
        if text[p:p + i+1] in tree.words.keys():
            i+=1
            cut_all(dict, text, dict_p, p, i)

    return dict_p


############
#   MAIN   #
############

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
        res_list.append(r[0])
        res_list=res_list+[r]
end = time.clock()
print('time to cut the sentence',end-start)

test_modification=cut_all(dict_chinese,"宁为玉碎不为瓦全")

"""
#study of the complexity in time : variation of the length of the sentence. 

sentence2 = ''.join(text)
sentence2 = sentence2[0:40]

x2=range(0,len(sentence2))
y2=[0 for j in range(0,len(sentence2))]
for i in range(5):
    for k in range(1,len(sentence2)):
        print(k)
        start = time.clock() 
        cut_all(dict_chinese,sentence2[0:k])
        end = time.clock()
        y2[k]=y2[k]+(end-start)
y2=[x/5 for x in y2]

plt.plot(x2,y1)
plt.plot(x2,y2)
plt.xlabel('Lenght of the sentence (nb of characters)')
plt.ylabel('Time (second)')
plt.show()

"""


