# -*- coding:utf-8 -*-

'''
写一个函数，它使用正则表达式，确保传入的口令字符串是强口令。强口令的
定义是：长度不少于 8 个字符，同时包含大写和小写字符，至少有一位数字。你可
能需要用多个正则表达式来测试该字符串，以保证它的强度。
'''

import re

re_length = re.compile(r'.{8,}')
re_alphabet = re.compile(r'[a-z].*[A-Z]]|[A-Z].*[a-z]')
re_num = re.compile(r'\d')


def strongPassword(password):
    if re_alphabet.search(password) and re_length.search(password) and re_num.search(password):
        print("密码验证成功")
    else:
        print("密码格式有误，请重新输入")

if __name__ == '__main__':
    password = input("请输入密码：")
    strongPassword(password)



