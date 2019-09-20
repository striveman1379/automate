1．空字典的代码是怎样的？
dict:{}

2．一个字典包含键'fow'和值 42，看起来是怎样的？
dict={'fow':42}

3．字典和列表的主要区别是什么？
字典是键值对形式的数据结构，无序的，根据键来存储数据，效率高
列表是有序的，可以根据索引查询数据，

4．如果 spam 是{'bar': 100}，你试图访问 spam['foo']，会发生什么？
会报错，KeyError错误

5．如果一个字典保存在 spam 中，表达式'cat' in spam 和'cat' in spam.keys()之间的区别是什么？
没有区别。in操作符检查一个值是不是字典中的一个键。

6．如果一个字典保存在变量中，表达式'cat' in spam 和'cat' in spam.values()之间的区别是什么？
'cat' in spam检查字典中是不是有一个'cat'键，而'cat' in spam.values()检查是否有一个值'cat'对应于spam中的某个键

7．下面代码的简洁写法是什么？
if 'color' not in spam:
spam['color'] = 'black'

spam.setdefault('color','black')
8．什么模块和函数可以用于“漂亮打印”字典值？
import pprint
pprint.pprint()
