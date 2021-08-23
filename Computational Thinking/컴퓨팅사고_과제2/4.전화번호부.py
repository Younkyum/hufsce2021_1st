fb = {"홍길동": "010-4444-5555","김중앙":"010-9191-8181","심청":"010-3232-5454"}
while True:
    w = 0
    name1 = input("이름>> ")
    for name in fb:
        if name1 in name:
            print(name, fb[name])
            w = 1
    if name1 == "add" :
        addingname = input("이름은? ")
        addphonenum = input("전화번호는? ")
        fb[addingname] = addphonenum
        print(addingname,"전화번호가 추가되었습니다.")
    elif w == 0:
        print("찾을 수 없습니다.")
