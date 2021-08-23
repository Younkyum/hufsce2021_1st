while True:
    a = []
    w = 0
    c = 0
    d = 0
    e = 0
    nn = ['', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    nnn = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    number = int(input("숫자는? "))
    numbert = format(number, ',')
    print(numbert)
    while number != 0 :
        a.append(number % 10)
        number = number // 10
    a.reverse()
    for i in a:
        for j in nnn:
            if i == j:
                a[a.index(i)] = nn[nnn.index(j)]
    for l in range(12-len(a)):
        a.insert(0,0)
    for k in a:
        e = e+1
        if e ==1 and k!=0:
            print(k,"천",sep='',end='')
            w = 1
        if e == 2 and k!=0:
            print(k,"백",sep='',end='')
            w = 1
        if e == 3 and k!=0:
            print(k,"십",sep='',end='')
            w = 1
        if e == 4 and k!=0:
            print(k,end='')
            w = 1
        if w == 1 and c == 0 and a.index(k)==3:
            print("억",end='')
            c = 1
        if e == 5 and k!=0:
            print(k,"천",sep='',end='')
            w = 2
        if e == 6 and k!=0:
            print(k,"백",sep='',end='')
            w = 2
        if e == 7 and k!=0:
            print(k,"십",sep='',end='')
            w = 2
        if e == 8 and k!=0:
            print(k,end='')
            w = 2
        if w == 2 and d == 0 and a.index(k) == 7:
            print("만",end = '')
            d = 1
        if e == 9 and k!=0:
            print(k,"천",sep='',end='')
        if e == 10 and k!=0:
            print(k,"백",sep='',end='')
        if e == 11 and k!=0:
            print(k,"십",sep='',end='')
        if e == 12 and k!=0:
            print(k,end='')

    print()