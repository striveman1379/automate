1．布尔数据类型的两个值是什么？如何拼写？
Ture和False

2．3 个布尔操作符是什么？
& | ！
and , or, not 

3．写出每个布尔操作符的真值表（也就是操作数的每种可能组合，以及操作
的结果）。

True and True 是 True。
True and False 是 False。
False and True 是 False。
False and False 是 False。
True or True 是 True。
True or False 是 True。
False or True 是 True。
False or False 是 False。
not True 是 False。
not False 是 True。




4．以下表达式求值的结果是什么？
(5 > 4) and (3 == 5)			false
not (5 > 4)				false
(5 > 4) or (3 == 5)			true
not ((5 > 4) or (3 == 5))		false
(True and True) and (True == False)	false
(not False) or (not True)		true



5．6 个比较操作符是什么？
=  !=  >  >=  <   <=

6．等于操作符和赋值操作符的区别是什么？
==   是等于操作符，它比较两个值，求值为一个布尔值
=    是赋值操作符，将值保存在变量中

7．解释什么是条件，可以在哪里使用条件。
条件是一个表达式，它用于控制流语句中，求值为一个布尔值

8．识别这段代码中的 3 个语句块：
spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')


执行后输出 spam


9．编写代码，如果变量 spam 中存放 1，就打印 Hello，如果变量中存放 2，就
打印 Howdy，如果变量中存放其他值，就打印 Greetings!

spam = int(input("请输入一个数字："))
if spam==1:
    print('hello')
elif spam==2:
    print("Howdy")
else:
    print('Greetings!')

10．如果程序陷在一个无限循环中，你可以按什么键？
ctrl+C

11．break 和 continue 之间的区别是什么？
break 跳出当前循环
continue 继续执行程序

12．在 for 循环中，range(10)、range(0, 10)和 range(0, 10, 1)之间的区别是什么？

没有区别

13．编写一小段程序，利用 for 循环，打印出从 1 到 10 的数字。然后利用 while
循环，编写一个等价的程序，打印出从 1 到 10 的数字。


for i in range(1,11):
	print(i)

---------
i=1
while i<11:
    print(i)
    i+=1


14．如果在名为 spam 的模块中，有一个名为 bacon()的函数，那么在导入 spam
模块后，如何调用它？
spam.bacon()

