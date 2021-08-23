loc = ['모현읍', '문형리', '분당동', '서현동', '규동']
while True:
    a = input("동을 입력하세요. ")
    if a in loc:
        idx = loc.index(a)+1
        print(idx,"번째 동입니다.",sep = '')
    else:
        print("새로운 동명입니다.",len(loc)+1,"번째 동으로 등록합니다.",sep='')
        loc.append(a)