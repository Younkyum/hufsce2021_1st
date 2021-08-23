# 202103378 진윤겸
word = []
wordcount = []
f = open("littleprince.txt", 'r')
lines = f.readlines()

for line in lines:
    line = line[:-1]
    sline = line.split(' ')
    for i in sline:
        if i in word:
            wordcount[word.index(i)] = wordcount[word.index(i)] + 1
        else:
            word.append(i)
            wordcount.append(1)

for i in range(10):
     a = max(wordcount)
     print(word[wordcount.index(a)], " : ", a)
     wordcount[wordcount.index(a)] = 0
