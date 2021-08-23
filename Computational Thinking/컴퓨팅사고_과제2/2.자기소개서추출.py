while True:
    intro = input("문장을 입력하세요 : ")
    sintro = intro.split()
    if sintro[0] == "저는":
        a = sintro[1].split("이")
        if len(a[0]) >= 6:
            a = sintro[1].split("입")

        print("이름 :",a[0])
    elif sintro[0] == "제":
        b = sintro[2].split("입")
        print("이름 :",b[0])
