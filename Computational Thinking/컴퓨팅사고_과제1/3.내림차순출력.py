line = []
print("데이터를 입력하세요(입력을 마치려면 0을 입력하세요)")
while True:
    a = int(input())
    if a == 0:
        line.sort(reverse=True)
        print("결과 ", end='')
        for i in line:
            print(i,end=' ')
        print("(",len(line),"개)",sep='')
        break
    else:
        line.append(a)