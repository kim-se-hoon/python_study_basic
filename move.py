'''
착한이사
1. 고객
2. 업체
입력: 1

1. 이사의뢰
2. 의뢰 내용 확인
입력: 1
연락처: 01012345678
이사 주소: 부산 진구 전포대로
이사 평수(평): 10
희망 가격(만원): 30
이사 의뢰가 완료 되었습니다.

입력: 2
연락처: 01012345678(입력)
이사 주소: 부산 진구 전포대로
이사 평수(평): 10
희망 가격(만원): 30
의뢰 가격: 35
업체 연락처: 01011112222

1. 고객
2. 업체
입력: 2
비밀번호: 2424(입력)
이사희망 리스트 확인
연락처: 01012345678
이사 주소: 부산 진구 전포대로
이사 평수(평): 10
희망 가격(만원): 30

연락처: 01012345679
이사 주소: 부산 진구 전포대로2
이사 평수(평): 15
희망 가격(만원): 35

입력할 견적의 순번을 입력하십시오(종료 q): 1
의뢰 가격: 35(입력)
업체 연락처: 01033004698(입력)
의로 완료


'''

class Move:
    def __init__(self):
        self.phone = ""
        self.address = ""
        self.houseSize = ""
        self.wishPayClient = ""
        self.wishPayCompany = ""
        self.companyPhone = ""

    def addClient(self, phone, address, houseSize, wishPayClient):
        self.phone = phone
        self.address = address
        self.houseSize = houseSize
        self.wishPayClient = wishPayClient

    def printMove(self):
        print("연락처:", self.phone)
        print("이사주소:", self.address)
        print("이사평수:", self.houseSize)
        print("희망가격:", self.wishPayClient)
        print("의뢰 가격:", self.wishPayCompany)
        print("업체 연락처:", self.companyPhone)

    def applyCompanyPay(self, wishPayCompany, companyPhone):
        self.wishPayCompany = wishPayCompany
        self.companyPhone = companyPhone
        print("업체 의뢰 완료")

moveList = []
while True:
    print("1.고객")
    print("2.업체")
    select = input("선택: ")

    if select == "1":
        print("1. 이사의뢰")
        print("2. 의뢰 내용 확인")
        select2 = input("선택: ")

        if select2 == "1":
            phone = input("연락처: ")
            address = input("이사주소: ")
            houseSize = input("이사 평수: ")
            wishPayClient = input("희망 가격: ")
            move = Move()
            move.addClient(phone, address, houseSize, wishPayClient)
            moveList.append(move)
        elif select2 == "2":
            findPhone = input("연락처: ")
            for i in range(len(moveList)):
                if moveList[i].phone == findPhone:
                    moveList[i].printMove()

    elif select == "2":
        checkPw = input("비밀번호: ")
        if checkPw == "2424":
            for i in range(len(moveList)):
                print("순번:", (i + 1))
                moveList[i].printMove()
                print()
            applyChoice = input("입력할 견적의 순번을 입력하십시오(종료 q):")
            if applyChoice == "q":
                continue
            else:
                applyChoiceInt = int(applyChoice)
                wishPayCompany = input("의뢰가격: ")
                companyPhone = input("업체 연락처: ")
                moveList[applyChoiceInt - 1].applyCompanyPay(wishPayCompany, companyPhone)
        else:
            print("비밀번호 오류, 접속 차단")





