def number():
    num = [1,2,-3,4,-5,6,-7,8,-9,10]
    positive = []
    negative = []
    for i in num:
        if i > 0 :
            positive.append(i)
        else:
            negative.append(i)
    return('Положительные числа %s , отрицательные числа %s' % (positive,negative))
print(number())