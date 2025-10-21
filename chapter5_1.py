'''
1. 회원 추가
2. 비밀번호 변경
3. 저장
'''

data = {
    "id" : "",
    "pw" : ""
}

'''
함수정의
signInUser(id):
    data 에 id를 넣는 로직

while 반복 1, 2, 3
'''

def signInUser(id, pw):
    data['id'] = id
    data['pw'] = pw

def changePw():
    # 여기서 아이디를 입력하고 아이디가 일치하면
    # 비밀번호 입력받아서 기존거 변경
    checkId = input("아이디: ")
    if checkId == data.get("id"):
        newPw = input("변경하고자 하는 비밀번호: ")
        data['pw'] = newPw
        print("비밀번호 변경 완료")
    else:
        print("존재하지 않는 아이디입니다.")

'''
유저확인 메소드(checkUser)
아이디: gildong
비밀번호: 1***
'''
def checkUser():
    print("아이디:", data.get('id'))
    print("비밀번호:", data.get('pw')[0], end="")
    for i in range(len(data.get("pw")) - 1):
        print("*", end="")
    print()

while True:
    print("1. 회원 추가")
    print("2. 비밀번호 변경")
    print("3. 저장")
    select = input("입력: ")
    if select == "1":
        signId = input("아이디 입력: ")
        signPw = input("비밀번호 입력: ")
        signInUser(signId, signPw)
    elif select == "2":
        changePw()
    elif select == "3":
        checkUser()




