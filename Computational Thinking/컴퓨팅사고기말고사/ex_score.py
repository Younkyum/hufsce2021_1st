import score as sc
ban = []
for i in range(5):
    student = []
    name = input("이름: ")
    kor_score = int(input("국어 점수: "))
    math_score = int(input("수학 점수: "))
    eng_score = int(input("영어 점수: "))
    student.append(name)
    student.append(kor_score)
    student.append(math_score)
    student.append(eng_score)
    student.append(sc.total(student))
    student.append(sc.ave(student))
    student.append(sc.grade(student))
    ban.append(student)
print()

for i in range(5):
    sc.output(ban[i])
print()

print("2명 성적 비교하여 더 좋은 점수의 학생 찾기")
sc.output(ban[2])
sc.output(ban[4])
print("성적이 더 좋은 학생")
sc.output(sc.max_student(ban[2], ban[4]))
print()

print("3명 성적 비교하여 더 좋은 점수의 학생 찾기")
sc.output(ban[1])
sc.output(ban[2])
sc.output(ban[3])
print("성적이 더 좋은 학생")
sc.output(sc.max_student(ban[1], ban[2], ban[3]))