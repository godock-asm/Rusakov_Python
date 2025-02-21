
def getmax():
    arr=[88, 7, 22568, 1254, 1]
    max = arr[0]
    for n in arr:
        if n > max:
            max = n
    return [max]
print(getmax())

print('______________________________')

def getmin():
    arr=[88, 7, 22568, 1254, 1]
    min = arr[0]
    for n in arr:
        if n < min:
            min = n
    return [min]
print(getmin())

print('______________________________')

def sum():
    array = [10, 5, 8, 4, 3]
    s = 0
    for i in array :
        s += i
        return [s]
print("Сумма чисел списка равна -", sum())