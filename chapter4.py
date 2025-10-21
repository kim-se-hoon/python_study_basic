''' 제어문(조건문) '''
# money = False
#
# if money:
#     print("택시를 타라")
# else:
#     print("걸어가라")

# money = False
# print("조건 전")
# if money:
#     print("택시를 타라")
#     print("집 도착")
# else:
#     print("걸어가라")
#     print("30분 걸림.....")
# print("조건 후")
#
# '''
# <if 문의 기본 구조>
# if 조건식:
#     수행할 문장1
#     수행할 문장2
#     ...
# else:
#     수행할 문장a
#     수행할 문장b
#     ...
#
# '''
#
# money = 4000
# if money >= 6000:
#     print("택시를 타라")
# else:
#     print("버스를 타라")
#
# '''
# 그리고 -> and
# 또는 -> or
# '''
# '''
# 돈이 6000원 이상 있거나 카드가 있으면 택시를 타라
#
# '''
# print()
# money = 3000
# card = True
#
# if money >= 6000 or card:
#     print("택시를 타라")
# else:
#     print("걸어가라")
#
# print()
#
# if money >= 6000:
#     print("택시를 타라")
# else:
#     print("현금이 6000 미만임")
#     if card:
#         print("카드 이용해서 택시탐")
#     else:
#         print("걸어감")
#
# print("입력: ", end="")
# insert = input()
# print(insert)
# print(type(insert))
# print(int(insert) == 6000)

print()
print([1, 2, 3])
print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])
print(not True)

'''
비밀번호 4자리 입력받기: 
숫자, 특수기호 따져서 다 되면 비밀번호 사용가능 출력
'''
'''
a2!3


'''
print("반복 전")
num = 0
while num < 20:
    print("%d 번째 손님입니다." %num)
    num = num + 1
print("반복 후")

print()
'''
홍길동 18세
홍길동 19세
홍길동 20세
홍길동 21세
홍길동 22세
'''
age = 0  # 초기문
while age < 5: # 조건식
    num = age + 18
    print("홍길동 %d세" %num)
    age = age + 1 # 후처리문

print()
menuList = {"americano" : 1500,
            "latte" : 3000,
            "chocolatte" : 4000}

'''
어서오세요 코리아카페입니다.
1. 가격확인
2. 포인트 충전
3. 포인트 잔액 확인
4. 주문
입력: 1

1. 아메리카노
2. 라떼
3. 초코라떼
입력: 1
1500원 입니다.

입력: 2
충전할 포인트를 입력하십시오: 5000

입력: 3
포인트 잔액 : 5000(출력으로 나옴)

입력: 4

1. 아메리카노
2. 라떼
3. 초코라떼
입력: 1
갯수: 3
아메리카노 3잔 나왔습니다.
포인트 잔액: 5500

'''
print()
print("어서오세요 코리아 카페입니다.")
money = 0
while True:
    print("1. 가격확인")
    print("2. 포인트 충전")
    print("3. 포인트 잔액 확인")
    print("4. 주문")
    print("q.종료")
    category = input("입력: ")

    if category == "1":
        print("1. 아메리카노")
        print("2. 라떼")
        print("3. 초코라떼")
        coffeeNum = input("입력: ")

        if coffeeNum == "1":
            print(menuList.get("americano"))
        elif coffeeNum == "2":
            print(menuList.get("latte"))
        elif coffeeNum == "3":
            print(menuList.get("chocolatte"))
        else:
            print("제공하지 않는 음료입니다.")

    elif category == "2":
        money += int(input("충전할 포인트를 입력하십시오: "))

    elif category == "3":
        print("잔액:", end="")
        print(money)

    elif category == "4":
        print("1.아메리카노")
        print("2.라떼")
        print("3.초코라떼")
        choiceMenu = input("입력: ")
        menuNum = int(input("갯수: "))

        if choiceMenu == "1":
            if (menuList.get("americano") * menuNum) > money:
                print("포인트가 부족합니다. 첫화면으로 이동합니다.")
                continue
            money = money - (menuList.get("americano") * menuNum)
            print("아메리카노 %d 잔 나왔습니다." %menuNum)
        elif choiceMenu == "2":
            if (menuList.get("latte") * menuNum) > money:
                print("포인트가 부족합니다. 첫화면으로 이동합니다.")
                continue
            money = money - (menuList.get("latte") * menuNum)
            print("라떼 %d 잔 나왔습니다." %menuNum)
        elif choiceMenu == "3":
            if (menuList.get("chocolatte") * menuNum) > money:
                print("포인트가 부족합니다. 첫화면으로 이동합니다.")
                continue
            money = money - (menuList.get("chocolatte") * menuNum)
            print("초코라떼 %d 잔 나왔습니다." %menuNum)
        else:
            print("없는 음료입니다.")
        print("포인트 잔액: %d" %money)
    elif category == "q":
        print("키오스크 종료합니다")
        break