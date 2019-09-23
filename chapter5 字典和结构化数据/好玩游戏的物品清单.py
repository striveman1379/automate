'''
你在创建一个好玩的视频游戏。用于对玩家物品清单建模的数据结构是一个字
典。其中键是字符串，描述清单中的物品，值是一个整型值，说明玩家有多少该物
品。例如，字典值{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}意味着玩
家有 1 条绳索、6 个火把、42 枚金币等。
写一个名为 displayInventory()的函数，它接受任何可能的物品清单，并显示如下： 第 5 章 字典和结构化数据 93
94 Python 编程快速上手——让繁琐工作自动化
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
'''


def displayinventory(dict):
    print("inventory:")
    totalVal = 0
    for key,value in dict.items():
        print(str(value) +"  "+ key)

        totalVal = totalVal + value
    print("Total number of items:",totalVal)

if __name__ == '__main__':
    dict = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    displayinventory(dict)
