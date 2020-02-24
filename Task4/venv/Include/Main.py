#преобразование целых тысяч
def thousandToRomain(n) :
    str = ''
    for i in range(n) :
        str += 'M'
    return str
#преобразование 500
def halfThToRomain(n, m2) :
    if m2 // 100 == 9 :
        return 'CM'
    elif n != 0:
        return 'D'
    else :
        return ''
#преобразование целых сотен
def hundredToRomain(n, m2) :
    if m2 // 100 == 9:
        return''
    elif n == 4 :
        return 'CD'
    else :
        str = ''
        for i in range(n) :
            str += 'C'
        return str

#преобразование 50
def halfHundredToRomain(n, d2) :
    if d2 // 10 == 9 :
        return 'XC'
    elif n != 0 :
        return 'L'
    else :
        return ''
#преобразование 10
def tenToRomain(n, d2) :
    if d2 // 10 == 9 :
        return ''
    if n == 4 :
        return 'XL'
    else :
        str = ''
        for i in range(n) :
            str += 'X'
        return str
#числа до 10
def numbersToRomain(n) :
    num = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    return num[n]

def arabicToRomain(number) :
    str = ''
    m1 = number // 1000;
    str += thousandToRomain(m1)
    m2 = number % 1000
    d1 = m2 // 500
    str += halfThToRomain(d1, m2)
    d2 = m2 % 500
    c1 = d2 // 100
    str += hundredToRomain(c1, m2)
    c2 = d2 % 100
    l1 = c2 // 50
    str += halfHundredToRomain(l1, c2)
    l2 = c2 % 50
    x1 = l2 // 10
    str += tenToRomain(x1, c2)
    x2 = l2 % 10
    str += numbersToRomain(x2)
    return str

def romainToArabic(number) :
    n = 0
    i = 0
    while i < len(number) :
        if(number[i] == "I") :
            n += 1
            if(i + 1 < len(number) and number[i + 1] == "V"):
                n += 3
                i += 1
            elif i + 1 < len(number) and number[i + 1] == "X" :
                n+=8
                i+=1

        elif(number[i] == "V") :
            n += 5
            i += 1
        elif number[i] == "X" :
            n += 10
            if(i + 1 < len(number) and number[i + 1] == "L") :
                n += 30
                i += 1
            elif  i + 1 < len(number) and number[i + 1] == "C" :
                n += 80
                i += 1

        elif number[i] == "L":
            n += 50

        elif number[i] == "C" :
            n += 100
            if(i + 1 < len(number) and number[i + 1] == "M") :
                n += 800
                i += 1
            elif(i + 1 < len(number) and number[i + 1] == "D") :
                n+= 400
                i+=1

        elif number[i] == "D" :
            n += 500

        elif number[i] == "M" :
            n += 1000
        i += 1
    return n


str = arabicToRomain(999)
print(str)
print(romainToArabic(str))