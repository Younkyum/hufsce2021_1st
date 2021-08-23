again = []
last = "apple"
while True:
    w = 0
    f = open("dict_test.TXT", 'r')
    answer = input("%s 끝말잇기? " % last)
    lastlet = last[4]
    if len(answer) == 5:
        if answer[0] == lastlet:
            if answer in again:
                print("중복된 단어입니다.(%s 의 끝말을 이으세요.)" % last)
            else:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    fw = line.split(":")
                    fws = fw[0].rstrip()
                    if fws == answer:
                        last = answer
                        again.append(answer)
                        w = 1
            if w == 1:
                print("정답입니다.(%s 의 끝말을 이으세요)" % last)
            else:
                print("사전에 없는 단어입니다.(%s 의 끝말을 이으세요.)" % last)
        else:
            print("단어가 틀려요.(%s 의 끝말을 이으세요)" % last)
            continue
    elif len(answer) > 5:
        print("단어가 길어요.(%s 의 끝말을 이으세요)" % last)
        continue
    else:
        print("단어가 짧아요.(%s 의 끝말을 이으세요)" % last)
        continue