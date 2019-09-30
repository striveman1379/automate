# -*- coding:utf-8 -*-

'''
写一个函数，它接受一个字符串，做的事情和 strip()字符串方法一样。如果只
传入了要去除的字符串，没有其他参数，那么就从该字符串首尾去除空白字符。否
则，函数第二个参数指定的字符将从该字符串中去除。

'''
import re

def strip_function(str, alphabet="\s"):
    rex = "^%s*|%s*$"%(alphabet,alphabet)
    #re_str为所自定义的正则模型     #re.compile('^\\s*|\\s*$') <class 're.Pattern'>
    re_str = re.compile(rex)
    #re.sub(pattern, repl, string, count=0, flags=0)
    # pattern: 正则中的模式字符串。
    # repl: 替换的字符串，也可为一个函数。
    # string: 要被查找替换的原始字符串。
    # count: 模式匹配后替换的最大次数，默认0表示替换所有的匹配。
    
    #re.sub()在这里的用法不是很理解
    str = re_str.sub('',str)
    return str

print(strip_function("    djjddd   "))
print(strip_function("1111dhddkj111",'1'))

