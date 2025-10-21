# 목데이터
data = {
    "location" : 2,
    "product" : [{"company": "lime", "num" : 10},
                 {"company": "beam", "num" : 20},
                 {"company": "singsing", "num" : 30},
                 {"company": "bird", "num" : 25}]
}

# 킥보드 어드민 어플
'''
1. 재고확인
2. 승차
3. 하차
입력: 1

위치 : 부산
lime 사 10개
beam 사 20개
singsing 사 30개
bird 사 25개

입력: 2
승차할 킥보드사를 입력하십시오: beam
(없으면, 존재하지 않는 킥보드사입니다. 출력)
갯수를 입력하십시오: 3
승차합니다.
승차합니다.
승차합니다.
(허위로 재고보다 더 많은 수 입력할 시 '재고가 틀렸습니다' 출력)
(기존 데이터도 변동되야함. 10 -> 7)

입력: 3
하차할 킥보드사를 입력하십시오: beam
갯수를 입력하십시오: 3
하차합니다.
하차합니다.
하차합니다.
(기존 데이터도 변동되야함. 7 -> 10)
'''

def printKickBoard():
    if data.get("location") == 2:
        print("위치: 부산")
    else:
        print("위치: 미정")
    for i in range(len(data.get("product"))):
        print(data.get("product")[i].get("company"), "사",
              data.get("product")[i].get("num"), "개")

while True:
    print("1.재고확인")
    print("2.승차")
    print("3.하차")
    select = input("입력: ")
    
    if select == "1":
        printKickBoard()

    elif select == "2":
        takingCompany = input("승차할 킥보드사를 입력하십시오: ")

        for i in range(len(data.get("product"))):
            if data.get("product")[i].get("company") == takingCompany:
                takingProductNum = int(input("갯수를 입력하십시오: "))
                if takingProductNum > data.get("product")[i].get("num"):
                    print("옳지 않은 갯수 입력")
                else:
                    data.get("product")[i]['num'] = data.get("product")[i].get("num") - takingProductNum
                    print("승차 완료")
                break

    elif select == "3":
        print("3번 선택")
    else:
        print("옳지 않은 입력입니다. 다시 입력하세요")
        continue








