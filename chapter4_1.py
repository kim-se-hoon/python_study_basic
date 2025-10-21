# while 문 빠져나가기

count = 5
print("뽑기기계 전")
while True:
    print("뽑기 팔이 내려옵니다~")
    count -= 1
    print("남은 횟수: %d" %count)

    if count == 0:
        print("뽑기 종료")
        break # 멈추고 반복문 1개 빠져나옴

print("뽑기기계 후")

print()
# while 문의 맨 처음으로 돌아가기
a = 0
while a < 10:
    num = a + 1
    a = a + 1
    if num % 2 == 0:
        continue
    print(num)

'''
입력받은 수의 홀수의 합을 구하시오
입력: 10
홀수의 합: 25
'''

# inputNum = int(input("입력: "))
# resultSum = 0
# i = 0
# while i < inputNum:
#     num = i + 1
#     i = i + 1
#     if num % 2 == 0:
#         continue
# 
#     resultSum += num
# 
# print("합:", resultSum)

'''
금액: 59990        (입력)
최소 지폐 갯수: 6 (출력)

'''
print("지폐 최소 갯수 세기")
money = int(input("금액: "))
moneyCount = 0

while True:
    if money >= 50000:
        money -= 50000
        moneyCount += 1
    elif money >= 10000:
        money -= 10000
        moneyCount += 1
    elif money >= 5000:
        money -= 5000
        moneyCount += 1
    elif money >= 1000:
        money -= 1000
        moneyCount += 1
    
    if money < 1000:
        break

print("계산 끝")
print(moneyCount)


