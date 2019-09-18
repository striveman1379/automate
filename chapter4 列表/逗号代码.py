# -*- coding:utf-8 -*-

'''
假定有下面这样的列表：
spam = ['apples', 'bananas', 'tofu', 'cats']
编写一个函数，它以一个列表值作为参数，返回一个字符串。该字符串包含所
有表项，表项之间以逗号和空格分隔，并在最后一个表项之前插入 and。例如，将
前面的 spam 列表传递给函数，将返回'apples, bananas, tofu, and cats'。但你的函数应
该能够处理传递给它的任何列表。
'''


spam = ['apples', 'bananas', 'tofu', 'cats']

def comma(spam):
    #pop()默认取出最后一个元素
    a = spam.pop()
    a = "and "+a
    # 最后一个元素做字符串拼接后重新添加到原列表
    spam.append(a)
    # 将", "插入到列表的每个元素之间
    blist = ", ".join(spam)
    return blist

if __name__ == '__main__':
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(comma(spam))
