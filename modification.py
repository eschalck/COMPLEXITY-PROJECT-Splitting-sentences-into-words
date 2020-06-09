import tree_dictionary as td
dict_chinese = td.dict_chinese
dict_flw={'为': ['玉', '瓦'],'我':['我'],'北':['京','京城'],'微分': ['别']}
def in_dict_f(word,wordbefore,dict_f):
    try:
        return word in dict_f[wordbefore]
    except KeyError:
        return False

def cut_modification(dict_f,dict,text,dict_p=None, p=0, i=1,thewordbefore=None):
    """
    a cut that give all the possibilities
    :param dict_f: dictionary some  words  of  the  dictionary  can’t  be  followed  by
    :param dict: dictionary tree
    :param text: a text without punctuations and ' '
    :param dict_p: a dictionary, keys : position pi, value : all the possible combination from the position
    :param p: a position
    :param i: length of word
    :return: dict_p: a dictionary that stocks all the possible combination from all positions
    """
    # initial only once
    if dict_p is None:
        dict_p = {}

    # real start
    print('p:',p,'i:',i)
    tree = dict.find_char(text[p:p+i])
    l_text=len(text)

    # stop condition
    if p+i == l_text and tree.is_word and not in_dict_f(tree.char,thewordbefore,dict_f):
        print(tree.char,thewordbefore)
        if p in dict_p.keys():
            dict_p[p] = dict_p[p] + [[tree.char]]
        else:
            dict_p[p]=[[tree.char]]
    else:
        if tree.is_word and not in_dict_f(tree.char,thewordbefore,dict_f):
            print(tree.char, thewordbefore)
            if p + i not in dict_p.keys():
                cut_modification(dict_f, dict, text, dict_p, p + i,1,tree.char)
            cut_list = []
            try:
                for l in dict_p[p + i]:
                    if len(l)==1:
                        if not in_dict_f(l[0],tree.char,dict_f):
                            cut_list.append([tree.char] + l)
                    else:
                        cut_list.append([tree.char] + l)
                if p in dict_p.keys():
                    dict_p[p] = dict_p[p] + cut_list
                else:
                    dict_p[p] = cut_list
            except KeyError:
                print('end')
    if text[p:p + i + 1] in tree.words.keys():
        cut_modification(dict_f,dict, text, dict_p, p, i + 1,thewordbefore)
    return dict_p

wo='我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我我'
mypoem = "爱情是蝴蝶恐惧是蜘蛛螃蟹可以狰狞牦牛会咆哮因为酸的猕猴桃和柠檬"
longword = "宁为玉碎不为瓦全"
jielong='北京城市场所有些微分别'
long41='汉语不同分支不一定能互通不过不同汉语分支的人一般通晓标准官话书面通用语通常指白话文'
d=cut_modification(dict_flw,dict_chinese, "宁为玉碎不为瓦全")
print(d)