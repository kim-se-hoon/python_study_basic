'''
[코인세탁소]
1. 세탁물 넣기
2. 세탁하기
3. 포인트 충전
4. 포인트 잔액 확인
q. 종료

입력: 1
세탁물의 무게를 입력하십시오(kg): 1

입력: 2
세탁강도(1.강, 2.중, 3.약): 1
세탁시간(1. 30분, 2. 1시간, 3. 1시간 30분): 2
(* 가격-> 무게 * 분 * 강도(강-150원, 중-100원, 약-50원)
가격: 9000원 (출력)

제휴사 할인이 있습니까?(1. kt, 2.회원, 3. 청년, 4. 없음): 1
(kt - 10%할인, 회원- 15%할인, 청년- 20%할인)
최종결제 금액: 9100원  (출력)

결제하시겠습니까?(1.네, 2.아니오): 1

돈있으면 -> 빨래를 시작합니다
없으면   -> 포인트가 부족합니다.(처음으로 돌아가기)

포인트 충전은 카페와 동일하게 진행
'''

while True:
    print("[코인세탁소]")
    print("1. 세탁물 넣기")
    print("2. 세탁하기")
    print("3. 포인트 충전")
    print("4. 포인트 잔액 확인")
    print("q. 종료")
    inputNum = input("입력: ")

    if inputNum == "1":
        washKG = int(input("세탁물의 무게를 입력하십시오(kg): "))
    elif inputNum == "2":
        washPower = input("세탁강도(1.강, 2.중, 3.약): ")
        washPowerMoney = 50
        if washPower == "1":
            washPowerMoney = 150
        elif washPower == "2":
            washPowerMoney = 100
        elif washPower == "3":
            washPowerMoney = 50
        washTime = input("세탁시간(1. 30분, 2. 1시간, 3. 1시간 30분): ")
        washTimeMoney = 30
        if washTime == "1":
            washTimeMoney = 30
        elif washTime == "2":
            washTimeMoney = 60
        elif washTime == "3":
            washTimeMoney = 90

        money = washKG * washPowerMoney * washTimeMoney
        print("가격:", money)

        washSaleCategory = input("제휴사 할인이 있습니까?(1. kt, 2.회원, 3. 청년, 4. 없음): ")
        finalMoney = 0
        if washSaleCategory == "1":
            finalMoney = 0.9 * money
        elif washSaleCategory == "2":
            finalMoney = 0.85 * money
        elif washSaleCategory == "3":
            finalMoney = 0.8 * money
        elif washSaleCategory == "4":
            finalMoney = money

        print("최종결제 금액:", finalMoney)
    elif inputNum == "3":
        print("3번 선택")
    elif inputNum == "4":
        print("4번 선택")
    elif inputNum == "q":
        print("q번 선택")
        break
    else:
        print("입력이 올바르지 않습니다.")
        continue
    






