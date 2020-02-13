def entering() :
    n = int(input("Введите кол-во строк во вложенном списке\n"))
    arr = []
    for i in range(n):
        l = [int(i) for i in input().split()]
        arr.append(l)
    return arr


def shift(arr, step) :
    if (step > 0):
        for i in range(step):
            arr.insert(0, arr.pop())
        for j in range(len(arr)):
            for k in range(step):
                arr[j].append(arr[j].pop(0))
    elif (step < 0) :
        for i in range(abs(step)):
            arr.append(arr.pop(0))
        for j in range(len(arr)):
            for k in range(abs(step)):
                arr[j].insert(0, arr[j].pop())
    return arr



arr = entering();
step = int(input("N = "))
print(arr[0])
print(shift(arr, step))


