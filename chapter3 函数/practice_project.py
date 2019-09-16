#Collatz 序列 和 输入验证

def collatz(number):
    if number % 2 == 0:
        res = number // 2
        return res
    elif number%2 ==1:
        res = 3 * number + 1
        return res
    elif number==1:
        return 1


try:
    number = int(input("Enter number：\n"))
    while True:
        number = collatz(number)
        print(number)

        if number==1:
            break
except ValueError:
    print("please input a right int number")
