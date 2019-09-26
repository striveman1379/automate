# -*- coding:utf-8 -*-

'this is a password locker program'

password = {
    'sina': 'sinaabc',
    'wangyi': 'wangyi123',
    'tencent': 'tencent456'
}

import pyperclip

if __name__ == '__main__':
    a = input("Please input your account：")
    if a in password:
        pyperclip.copy(password[a])
        print('password for %s copied for clipboard'%a)
    else:
        print('there is no account %s'%a)

        try:
            an = input("Do you want to add this account in passwd? yes/no")
            if an == "no":
                print('thanks for using password locker')
            elif an == 'yes':
                print('this function has not develped yet')
        except:
            print('exit program')





