all_score = []
while True:
    filename = input("열 파일 이름을 입력하시오.")
    makefile = input("만들 파일 이름을 입력하시오.")
    try:
        mf = open(makefile, 'w')
        mfs = mf.readline()
        userp = input("이미 존재하는 파일입니다. 덮어쓰려면 1을 입력해주세요. ")
        mf.close()
        if userp == "1":
            pass
        else:
            print("프로그램을 종료합니다.")
            break
    except:
        try:
            f = open(filename, encoding='UTF8')
            while True:
                fh = f.readline()
                if fh == '':
                    break
                fh = fh[:-1]
                s = fh.split(",")
                all_score.append(s)
            for i in range(10):
                total = int(all_score[i][1]) + int(all_score[i][2]) + int(all_score[i][3])
                all_score[i].append(total)
                all_score[i].append(int(total/3))
            all_score.sort(reverse= True, key=lambda x:x[5])
            f.close()
            mf = open(makefile, 'w', encoding='UTF8')
            mf.write("성적표(학번순)\n")
            mf.write("  학번   국어 수학 영어 총합 평균 석차\n =========================================================\n")
            for i in range(10):
                all_score[i].append(i+1)
            all_score.sort(key=lambda x:x[0])
            for j in all_score:
                k = "  ".join((map(str, j)))
                k = k + "\n"
                mf.write(k)
            mf.close()
            break
        except:
            print("열 수 없는 파일입니다. 파일이 존재하지 않습니다.")
