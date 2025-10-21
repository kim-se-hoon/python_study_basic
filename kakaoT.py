'''
1. 일반(4,800원)
2. 블루(5,400원)
3. 블랙(6,400원)
4. 대형(6,600원)
원하시는 택시를 입력하십시오: 1
일반 택시에 탑승 하였습니다.

1. 일반(100m 당 100원)
2. 블루(100m 당 110원)
3. 블랙(100m 당 120원)
4. 대형(100m 당 130원)
이동한 거리를 입력하십시오: 3000

금액: 7800원

'''

# totalPay = 0
#
# print("입력: ", end="")
# insert = input()
# if insert == "1":
#     totalPay = 4800
# print(totalPay)
'''
영수증
{
    차량번호: 182부4302,
    택시 종류: 일반,
    기본 가격: 4800,
    이동거리 가격: 1000,
    총 가격: 5800
}
'''
kakaoDic = {}
basicPay = 0
distancePay = 0
print("차량번호: ", end="")
carNumber = input()
kakaoDic["차량번호"] = carNumber
print("1. 일반(4,800원)")
print("2. 블루(5,400원)")
print("3. 블랙(6,400원)")
print("4. 대형(6,600원)")
print("입력: ", end="")
category = input()

if category == "1":
    kakaoDic["택시 종류"] = "일반"
    basicPay = 4800
else:
    if category == "2":
        kakaoDic["택시 종류"] = "블루"
        basicPay = 5400
    else:
        if category == "3":
            kakaoDic["택시 종류"] = "블랙"
            basicPay = 6400
        else:
            if category == "4":
                kakaoDic["택시 종류"] = "대형"
                basicPay = 6600
            else:
                print("지원하지 않는 택시입니다.")

kakaoDic["기본 가격"] = basicPay
print("1. 일반(100m 당 100원)")
print("2. 블루(100m 당 110원)")
print("3. 블랙(100m 당 120원)")
print("4. 대형(100m 당 130원)")
print("이동한 거리를 입력하십시오: ", end="")
distance = int(input())

if category == "1":
    distancePay = distance
elif category == "2":
    distancePay = distance * 1.1
elif category == "3":
    distancePay = distance * 1.2
elif category == "4":
    distancePay = distance * 1.3
else:
    print("차량 x")
kakaoDic["이동거리 가격"] = distancePay
kakaoDic["총 가격"] = basicPay + distancePay
print("총금액: ", (basicPay + distancePay))

print()
print(kakaoDic)










