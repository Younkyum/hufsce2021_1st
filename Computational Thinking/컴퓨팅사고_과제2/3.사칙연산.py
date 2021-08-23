while True:
    s = 0
    total = 0
    c = []
    a = input("수식을 입력하세요 : ")
    b = a.split("+")
    for i in b:
        c.append(i.split("-"))
    for j in c:
        if len(j)>1:
            for k in j:
                if j.index(k) == 0:
                    s = int(k)
                else:
                    s = s-int(k)
            c[c.index(j)] = s
        else:
            c[c.index(j)] = j[0]
    for l in c:
        total = total + int(l)
    print(total)