'''
점수가 89점 초과이면 A학점
점수가 79점 초과이면 B학점
점수가 69점 초과이면 C학점
점수가 59점 초과이면 D학점
그 이하이면 F학점
단, 점수가 100점 초과이거나 0점 미만이면 계산불가 출력

점수: 77
학점: C학점

점수: 200
학점: 계산불가

'''
print("점수: ", end="")
score = int(input())
result = ""

if score > 100 or score < 0:
    result = "계산불가"
elif score > 89:
    result = "A학점"
elif score > 79:
    result = "B학점"
elif score > 69:
    result = "C학점"
elif score > 59:
    result = "D학점"
else:
    result = "F학점"
print(result)









