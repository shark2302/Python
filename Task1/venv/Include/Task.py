def loop(list, n) :
    if(n > 0):
        for i in range(n) :
            list.insert(0, list.pop())
    elif(n < 0) :
        for i in range(abs(n)) :
            list.append(list.pop(0))
    return list



list  = [int(i) for i in input('Введите элементы списка \n').split()]
n = int(input('Введите n : \n'))
print(loop(list, n))