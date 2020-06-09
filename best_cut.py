import tree_dictionary as td
dict_chinese=td.dict_chinese

def remove_punctuation(string):
    """
    Function to remove punctuations
    :param string: a string with punctuations
    :return: the string without punctuations
    """
    # punctuation marks
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~，。、_-'''
    for x in string:
        if x in punctuations:
            string = string.replace(x, " ")
    return string


def find_word(tree,text,p):
    global found, res
    found = False
    l = len(tree.char)
    if text[p:p + l + 1] in tree.words.keys():
        find_word(tree.words[text[p:p + l + 1]], text, p)
    if found:
        return res
    else:
        if tree.is_word:
            found = True
            print('found word', tree.char, p + l)
            res = p + l
        elif len(tree.char) == 1:
            found = True
            print('went wrong, go backwards')
            res = p - 1
        if found:
            return res

def backwards(dict,wordlist,text,p):
    lastword=wordlist.pop(-1)
    print('lastword',lastword)
    l = len(lastword) - 1

    for i in range(l):
        tree = dict.find_tree(text[p-i])
        new_p=find_word(tree, text, p - i)
        if dict.find_char(lastword[:l-i]).is_word and new_p > p-i:
            print(lastword[:l])
            return lastword[:l], p-i
    return backwards(dict,wordlist,text,p-l-1)

#test find_tree() and find_word()
#tree=find_tree(dict_chinese,'哪')
#print(tree.char)
#find_word(tree,'和尚去哪里',3)
def cut(dict,text):
    wordlist=[]
    p=0
    l_text=len(text)
    while p<l_text and p>=0:
        tree=dict.find_tree(text[p])
        new_p=find_word(tree,text,p)
        if new_p>p:
            new_word=text[p:new_p]
        else:
            new_word,new_p=backwards(dict,wordlist,text,new_p)
        wordlist.append(new_word)
        p=new_p
    return wordlist

#main

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
text=remove_punctuation(sentence).split(' ')
res = []
for sub_text in text:
    res=res+cut(dict_chinese,sub_text)
print(res)
#test go backwards
#t=find_tree(dict_chinese,'别')
#t.is_word=False
#cut(dict_chinese,text)