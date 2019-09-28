1．创建 Regex 对象的函数是什么？
re.compile() 函数返回Regex对象

2．在创建 Regex 对象时，为什么常用原始字符串？
使用原始字符串是为了让反斜杠不必转义

3．search()方法返回什么？
返回Match对象

4．通过 Match 对象，如何得到匹配该模式的实际字符串？
group()

5．用 r'(\d\d\d)-(\d\d\d-\d\d\d\d)'创建的正则表达式中，分组 0 表示什么？分组 1
呢？分组 2 呢？
0 表示整个匹配结果
1 包含第一组括号
2 包含第二组括号

6．括号和句点在正则表达式语法中有特殊的含义。如何指定正则表达式匹配
真正的括号和句点字符？
句号和括号可以用反斜杠转义：\.    \(和\)

7．findall()方法返回一个字符串的列表，或字符串元组的列表。是什么决定它
提供哪种返回？
如果正则表达式没有分组，就返回字符串的列表。
如果正则表达式有分组，就返回字符串的元祖的列表

8．在正则表达式中，|字符表示什么意思？
| 字符表示匹配两个组中的“任何一个”

9．在正则表达式中，?字符有哪两种含义？
？ 匹配0次或1次，或用于表示非贪心匹配

10．在正则表达式中，+和*字符之间的区别是什么？
+ 表示贪婪匹配，匹配1次或多次
* 表示0次或多次

11．在正则表达式中，{3}和{3,5}之间的区别是什么？
{3} 匹配前面分组的精确三次实例
{3,5} 匹配3-5次实例

12．在正则表达式中，\d、\w 和\s 缩写字符类是什么意思？
\d   匹配一个数字
\w 	单词
\s  空白字符

13．在正则表达式中，\D、\W 和\S 缩写字符类是什么意思？
缩写字符分类\D、\W 和\S 分别匹配一个字符，它不是数字、单词或空白
字符

14．如何让正则表达式不区分大小写？
re.I 或 re.IGNORECASE 作为第二个参数传入re.compile()，让匹配不区分大小写

15．字符.通常匹配什么？如果 re.DOTALL 作为第二个参数传递给 re.compile()，
它会匹配什么？
字符. 匹配任何字符，除了换行符
如果 re.DOTALL 作为第二个参数传递给 re.compile()，那么点也会匹配换行符

16．.*和.*?之间的区别是什么？
.*执行贪心匹配
.*?执行非贪心匹配

17．匹配所有数字和小写字母的字符分类语法是什么？
[0-9a-z]或者[a-z0-9]

18．如果 numRegex = re.compile(r'\d+')，那么 numRegex.sub('X', '12 drummers, 11 
pipers, five rings, 3 hens')返回什么？

X drummers, X pipers, five rings, X hens      #re.sub()可re.sub()方法不仅可以对一种字符串进行替代，还可以替代多种字符串替换

19．将 re.VERBOSE 作为第二个参数传递给 re.compile()，让你能做什么？

re.VERBOSE 参数允许为传入 re.compile() 的字符串添加空格和注释。

20．如何写一个正则表达式，匹配每 3 位就有一个逗号的数字？它必须匹配以
下数字： '42'
 '1,234'
 '6,368,745'
但不会匹配：  '12,34,567' （逗号之间只有两位数字）  '1234' （缺少逗号）

re.compile(r^\d{1,3}(,\d{3})*$)

21．如何写一个正则表达式，匹配姓 Nakamoto 的完整姓名？你可以假定名字
总是出现在姓前面，是一个大写字母开头的单词。该正则表达式必须匹配：  'Satoshi Nakamoto'
 'Alice Nakamoto'
 'RoboCop Nakamoto'
但不匹配：  'satoshi Nakamoto'（名字没有大写首字母）  'Mr. Nakamoto'（前面的单词包含非字母字符）
 'Nakamoto' （没有名字）  'Satoshi nakamoto'（姓没有首字母大写）

re.compile(r'[A-Z][a-z]*\sNakamoto')


22．如何编写一个正则表达式匹配一个句子，它的第一个词是 Alice、Bob 或
Carol，第二个词是 eats、pets 或 throws，第三个词是 apples、cats 或 baseballs。该句
子以句点结束。这个正则表达式应该不区分大小写。它必须匹配：
 'Alice eats apples.'
 'Bob pets cats.'
 'Carol throws baseballs.'
 'Alice throws Apples.'
 'BOB EATS CATS.'
但不匹配： 
 'RoboCop eats apples.'
 'ALICE THROWS FOOTBALLS.'
 'Carol eats 7 cats.'

re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.',re.IGNORECASE)


