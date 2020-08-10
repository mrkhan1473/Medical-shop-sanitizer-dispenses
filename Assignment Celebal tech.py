# this assignment about to get the total number of Sanitizer bottles and Size

def bottles(var1):
    size10 = var1 // 10
    var1 = var1 % 10

    size7 = var1 // 7
    var1 = var1 % 7

    size5 = var1 // 5
    var1 = var1 % 5

    size3 = var1 // 3
    var1 = var1 % 3

    size1 = var1

    return size10, size7, size5, size3, size1


def result(var2, var3, var4, var5, var6):
    if var2 == 0:
        pass
    else:
        print("10 liters = ", var2, end=",")
    if var3 == 0:
        pass
    else:
        print(" 7 liters = ", var3, end=",")
    if var4 == 0:
        pass
    else:
        print(" 5 liters = ", var4, end=",")
    if var5 == 0:
        pass
    else:
        print(" 3 liters = ", var5, end=",")
    if var6 == 0:
        pass
    else:
        print(" 1 liters = ", var6, end=",")

    print(" Total number of bottles : ", var2+var3+var4+var5+var6)


user_input = int(input("Enter total liters of sanitizer :- "))

a, b, c, d, e = bottles(user_input)

result(a, b, c, d, e)
