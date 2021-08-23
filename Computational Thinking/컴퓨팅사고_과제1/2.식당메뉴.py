menu = ["noodle", "ham", "egg", "spaghetti"]
price = [500, 200, 100, 900]
while True:
    print("안녕하세요 다음의 메뉴 중 원하는 메뉴를 선택하세요.")
    a = input("(noodle, ham, egg, spaghetti) ")
    if a in menu:
        idx = menu.index(a)
        print(price[idx],"원입니다.",sep='')
    else:
        print("그런 메뉴는 없습니다.")
    print()