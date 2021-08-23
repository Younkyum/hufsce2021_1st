num = set(range(2, 100000))

for i in range(2,100000):
    if i in num:
        num = num - set(range(2*i, 100000, i))
print(len(num))