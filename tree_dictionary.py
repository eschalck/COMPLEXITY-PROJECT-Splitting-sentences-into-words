import pandas as pd
import time
#f=open('dict.txt.small.txt')
#text=f.read()

data = pd.read_csv('dict.txt.small.txt', sep=" ", header=None)
data.columns = ["word", "frequency", "pos"]
class Character:
    """
    can be seen as a node of tree
    it has its character/characters (string) and if it's a word (boolean) as attributes
    words is a dict of its branch
    """
    def __init__(self,characters):
        self.char=characters
        self.is_word=False
        self.words={}

    def find_branch(self, char):
        """
        give a string character and its mother tree find the Character object
        :param tree: mother tree
        :param char: string character
        :return: Character object
        """
        lt = len(self.char)
        lb = len(char)
        if lt == lb:
            return self
        else:
            try:
                return self.words[char[:lt + 1]].find_branch(char)
            except:
                print('can not find')
                return Character(char[:lt + 1])


    def add_word(self, word):
        """
        a recursive function
        add a new word to a character tree
        :param mother: a character object, begin with the same character as word
        :param word: a chinese word string
        :return: no return value
        """
        if self.char == word:
            self.is_word = True
        else:
            l = len(self.char)
            if word[:l + 1] not in self.words.keys():
                new = Character(word[:l + 1])
                self.words[word[:l + 1]] = new
                return new.add_word(word)
            else:
                return self.words[word[:l + 1]].add_word(word)


class Dict_tree:
    def __init__(self):
        self.character_dict={}
    def add_character(self,characters):

        if characters[0] not in self.character_dict.keys():
            mother = Character(characters[0])
            self.character_dict[characters[0]]=mother
        else:
            mother = self.character_dict[characters[0]]
        mother.add_word(characters)

    def find_tree(self, char):
        """
        give a character string length 1 , return to its Character object in dict
        :param dict: dictionary of length 1 Character object
        :param char: a character string length 1
        :return: Character object
        """
        try:
            return self.character_dict[char]
        except:
            return Character(char)


    def find_char(self, char):
        '''
        give a string character find the Character object
        :param dict: dictionary of length 1 Character object
        :param char: string character
        :return: Character object
        '''
        tree = self.find_tree(char[0])
        return tree.find_branch(char)

    def find_max_sub_word(self, char):
        """
        find the longest word shorter than given string
        :param char: a string
        :return: the longest word shorter than the string
        """
        l = len(char) - 1
        while l > 0 and not self.find_char(char[:l]).is_word:
            l -= 1
        return char[:l]

# build tree
    
start=time.clock() 
dict_chinese=Dict_tree()
for word in data['word']:
    dict_chinese.add_character(word)
end=time.clock() 
print('time to build the tree',end-start)

"""
total=0
for k in range(5):
    start=time.clock() 
    dict_chinese=Dict_tree()
    for word in data['word']:
        dict_chinese.add_character(word)
    end=time.clock() 
    total=total+(end-start)
print('time to build the tree',total/5)
"""
