# -*- coding:utf-8 -*-

'''
写一个名为 addToInventory(inventory, addedItems)的函数，其中 inventory 参数
是一个字典，表示玩家的物品清单（像前面项目一样），addedItems 参数是一个列表，
就像 dragonLoot。
addToInventory()函数应该返回一个字典，表示更新过的物品清单。请注意，列
表可以包含多个同样的项。你的代码看起来可能像这样：
def addToInventory(inventory, addedItems):
# your code goes here
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
前面的程序（加上前一个项目中的 displayInventory()函数）将输出如下：
Inventory:
45 gold coin
1 rope
1 ruby
1 dagger
Total number of items: 48

'''



#addToInventory函数参数1为字典，参数2为列表，循环此列表，将列表中的数据添加到字典
def addToInventory(inventory,addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i]+=1
        else:
            inventory[i]=1
    return inventory


#该函数展示字典的结果，并对字典中各个结果的值进行累加
def displayInventory(dict):
    print("inventory:")
    totalVal = 0
    for key,value in dict.items():
        print(str(value) +"  "+ key)

        totalVal = totalVal + value
    print("Total number of items:",totalVal)


if __name__ == '__main__':
    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = addToInventory(inv, dragonLoot)
    displayInventory(inv)
