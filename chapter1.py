print("hihi2")

x = 3
y = x + 3
print(y)
x = 10
y = x + 3
print(y)
print(y)

# 주석: 코드 실행 결과에 영향을 미치지 않는 부분을 작성할 때 사용
'''
주석 작성법
-> #주석내용, '''''', """ 주석내용 """
-> 주석 단축키 : ctrl + /
'''
appleBananaJuice = 15
print(appleBananaJuice)

# 자동완성 단축키 -> ctrl + space

''' 숫자형 자료형 '''
# 뺄셈
a = 10
b = 5
c = a - b
print(c)

# 곱셈
a = 2
b = 3
c = a * b
print(c)
c = a ** b  # ** -> 제곱
print(c)

# 나눗셈
a = 10
b = 2
print(a / b)

x = 7
y = 3
print(x / y)
print(x // y) # // -> 몫을 구하는 연산자
print(x % y) # % -> 나머지를 구하는 연산자

''' 문자열 자료형'''
'''
문자열: 문자, 단어 등으로 구성된 문자들의 집합을 의미
문자열을 만드는 방법: "", '', """""", ''''''
'''
str2 = "Life is too short, You need Python"
print(str2)
# 길동이 말합니다 "안녕 친구들"

str3 = 'gildong says "hihi"'
print(str3)

'''
apple
banana
juice
'''
print("""appple
banana
juice""")
print()
print("apple\nbanana")

# 길동의 사과
# gildong's apple
print('gildong\'s apple')

print()

# 문자열 연산
head = "Python "
tail = "is fun!"
print(head + tail)
print(head * 2)

''' 문자열 인덱싱과 슬라이싱'''
a = "Life is too short, You need Python"

# 인덱스는 0부터 시작함.
print(a[3])
print(a[0])
print(a[-1])

k = a[0] + a[1] + a[2] + a[3]
print(k)

# 3번 전까지 잘라라는 말이다.
t = a[0:3]
print(t)

t2 = a[0:4]
print(t2)

a = "Python is fun!"
print(len(a))
print(a[7:14])
print(a[7:len(a)])
print(a[7:])
print(a[:7])
print(a[:])
print(a)

## 일자 날씨 출력 예제
a = "20250504veryverycold"

# 2025-0504
# 2025-0504:15:48:45
# 2025-5-4
'''
date와 weather를 출력하시오
일자: 20250504
날씨: Rainny
'''
print("날짜: " + a[:8])
print("날씨: " + a[8:])
print()
print("날짜: " + a[:8] + "\n" + "날씨: " + a[8:])


# 현재 온도는 19도 입니다.
# 현재 온도는 20도 입니다.
# 현재 온도는 17도 입니다.
# 문자열 포메팅: 문자열 안에 어떤 값을 삽입하는 방법
print()
## 숫자 대입
a = "I eat %d apples" %3
print(a)

## 문자 대입
b = "I eat %s apples" %"five"
print(b)

## 숫자 값을 나타내는 변수 대입
num = 5
a = "I eat %d apples" %num
print(a)

## 2개 이상의 값 넣기
number = 10
day = "three"
d = "I ate %d apples. so I was sick for %s days" %(number, day)
print(d)


## format 함수를 사용한 포메팅
# 숫자 대입
a = "I eat {0} apples".format(3)
print(a)

# 문자 대입
b = "I eat {0} apples".format("five")
print(b)

# 숫자값을 가진 변수 대입
number = 3
c = "I eat {0} apples".format(number)
print(c)

# 2개 이상 값 넣기
number = 10
day = "three"
d = "I ate {0} apples. so I was sick for {1} days".format(number, day)

d2 = ("I ate {count} apples. so I was sick for {dayNum} days"
      .format(count = 10, dayNum = 20))
print(d2)

print()
''' 문자열 관련 함수들 '''
## 문자 갯수 세기(count)
a = "hobby"
print(a.count("b"))
print(a.count("h"))

# 위치 알려주기(find)
a = "Python is the best choice"
print(a.find("b"))
print(a.find("k")) # 없으면 -1
print(len(a))
print(a.rfind("c"))

print()
url = "https://news.naver.com/section/105"
# url의 뒤 숫자를 출력하시오
index = url.rfind("/")
print(url[index + 1 :])














