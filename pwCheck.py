numList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
tList = ["!", "@", "#", "$", "%", "^", "&", "*"]

checkFlag1 = False
checkFlag2 = False
pw = input("비밀번호를 입력하시오: ")
# print(pw)
# print(type(pw))
# print(pw[0:1] in numList)

checkChar = pw[0:1]

if checkChar in numList:
    checkFlag1 = True
    print("숫자 포함")
elif checkChar in tList:
    checkFlag2 = True
    print("특수기호 포함")

checkChar = pw[1:2]

if checkChar in numList:
    checkFlag1 = True
    print("숫자 포함")
elif checkChar in tList:
    checkFlag2 = True
    print("특수기호 포함")

checkChar = pw[2:3]

if checkChar in numList:
    checkFlag1 = True
    print("숫자 포함")
elif checkChar in tList:
    checkFlag2 = True
    print("특수기호 포함")

checkChar = pw[3:4]
if checkChar in numList:
    checkFlag1 = True
    print("숫자 포함")
elif checkChar in tList:
    checkFlag2 = True
    print("특수기호 포함")

result = checkFlag1 and checkFlag2

if result:
    print("비밀번호 사용가능")
else:
    print("사용 불가능")


















