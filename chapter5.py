def add(a, b):
    print("안녕안녕")
    return a + b

'''
함수명: add
매개변수: a, b
리턴값: a + b
'''
print(add(10, 20))
print()
add(20, 30)

print()
''' 매개변수가 없는 함수 '''
def hi():
    return "hi"

a = hi()
print(a)

''' 리턴값이 없는 함수 '''
def add2(a, b):
    print(a)
    print(b)

print(add2(10, 20))

''' 매개변수 지정하여 호출하기 '''
def minus(a, b):
    return a - b

print(minus(10, 7))
print(minus(b = 7, a = 3))
print()
''' 입력값의 갯수를 모르는 경우 '''

def many(*args):
    for i in args:
        print(i)

many(2, 3, 4, 7, 7)

'''
나이들을 받는 함수를 만드시오
함수명: many_age

출력으로 받은 나이들 하나씩 출력하십시오
그리고 리턴으로 받은 나이들의 평균값을 리턴하고
최종적으로 그 값을 출력하십시오

many_age(20, 22, 24, 17, 18)

'''
print()
def many_age(*args):
    sumAge = 0
    for i in args:
        print(i)
        sumAge += i
    return sumAge / len(args)

avgAge = many_age(20, 22, 24, 17, 18, 40)
print(avgAge)

'''
cal(add, 1, 2)
cal(min, 1, 2)
'''
def cal(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
        return result
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
        return result
print(cal("add", 2, 3, 7, 7))
print(cal("mul", 3, 3, 3))


print()
a = 1
def test_k(k):
    k += 1
    return k
print(test_k(a))
print(a)

v = 5
def test_v():
    global v
    v = v + 1

test_v()
print(v)

print()
''' 람다식 '''
def add3(a, b):
    return a + b

add4 = lambda a, b : a + b
print(add4(10, 20))

hi = lambda t : "%s입니다" %t
print(hi("홍길동"))








