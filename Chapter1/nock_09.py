# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．

#!usr/bin/env python
# -*- coding:utf-8 -*-
import random
charstring = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
def sort(char):
    if len(char)<=4:
        return char
    else:
        wordlist=list(char[1:-1])
        random.shuffle(wordlist)
        return char[0]+''.join(wordlist)+char[-1]
sortword=""
for string in charstring.replace("."," .").split():
    sortword+= " "+sort(string)
print(sortword)
