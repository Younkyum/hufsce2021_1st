import phonebook

myPhoneBook = phonebook.PhoneBook()       # 전화번호부 객체 생성하기

# 홍길동 번호 만들기
oneperson = phonebook.Phone("홍길동", "010-5555-2222")
myPhoneBook.addPerson(oneperson)

# 강감찬 번호 만들기
twoperson = phonebook.Phone("강감찬", "010-2222-3333")
myPhoneBook.addPerson(twoperson)

# 심청 전화번호 만들기
threeperson = phonebook.Phone("심청", "010-3333-2222")
myPhoneBook.addPerson(threeperson)

# 전화번호 출력하기
for i in range(myPhoneBook.getBookCount()):
    myPhoneBook.getBook(i).printPerson()
