'''
1. 주차하기
2. 정산
입력: 1

차 번호: 118부1234(입력)
주차시각: ~~~~ (출력)
차량 번호: 118부1234(출력)


'''
import parkLogic
import time
while True:
    print("1. 주차")
    print("2. 정산")
    select = input("입력: ")
    if select == "1":
        num = input("차량번호: ")
        parking = parkLogic.SingletonClass()
        print(parking)
        parking.inputCar(time.ctime(), num)

    '''
    2. 정산
    차량번호: 1111(입력)
    가격: 6000원(30분당 1000원)
    입금: 6000
    *돈을 parkLogic에서 받아서 payDB로 전달, 정산하면 차 제거
    
    3. 주차장 총 매출
    매출: 10000원
    parkLogic을 들려서 payDB에서 값을 가져와서 보여주기
    '''









