1．什么是转义字符？
转义字符表示字符串中的一些字符，这些字符用别的方式很难在代码中打出来

2．转义字符\n 和\t 代表什么？
\n 代表换行
\t 制表符

3．如何在字符串中放入一个倒斜杠字符\？
\\ 转义字符表示一个反斜杠

4．字符串"Howl's Moving Castle"是有效字符串。为什么单词中的单引号没有转义，却没有问题？
Howl's中的单引号没有问题，因为你用了双引号来表示字符串的开始和结束

5．如果你不希望在字符串中加入\n，怎样写一个带有换行的字符串？
多行字符串让你在字符串中使用换行符，而不必用\n转义字符

6．下面的表达式求值为什么？
• 'Hello world!'[1]		e
• 'Hello world!'[0:5]		Hello
• 'Hello world!'[:5]		Hello
• 'Hello world!'[3:]		lo world!

7．下面的表达式求值为什么？
• 'Hello'.upper()			HELLO
• 'Hello'.upper().isupper()		Ture
• 'Hello'.upper().lower()		hello

8．下面的表达式求值为什么？
• 'Remember, remember, the fifth of November.'.split()
['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']

• '-'.join('There can be only one.'.split())
'There-can-be-only-one.'

9．什么字符串方法能用于字符串右对齐、左对齐和居中？
rjust()    ljust()     center()

10．如何去掉字符串开始或末尾的空白字符？
lstrip()
rstrip()

