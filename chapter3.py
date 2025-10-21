'''
튜플
: 리스트는 요솟값의 변화가 가능하고
  튜플은 요솟값의 변화가 불가능하다.
값이 바뀌지 않았으면 하는것들을 넣어두면 된다.

-> 리스트는 대괄호([])로 둘러싸지만
   튜플은 소괄호(())로 둘러싼다.
-> 리스트는 요소 값의 생성, 삭제, 수정이 가능하지만
   튜플은 생성, 삭제, 수정이 불가능하다.
'''

t = (1, 2, 3)
print(t)
t2 = 1, 2, 3 #튜플은 소괄호 생략이 가능하다.
print(t2)

t3 = (4,) # 요솟값이 하나일때는 콤마를 반드시 붙여야함.
print(t3)

t = (1, 2, 3)
# del t[0] 튜플 삭제 안되는거 확인
# t[0] = 100 튜플 값 수정 안되는거 확인

# 튜플의 인덱싱과 슬라이싱
t1 = (1, 2, 'a', 'b')
print(t1[3])

print(t1[1:3])

# 튜플 더하기
t2 = (3, 4)
t3 = t1 + t2
print(t3)

# 튜플 곱하기
print(t3 * 3)

# 튜플 길이구하기
print(len(t3))

'''
딕셔너리란?
"이름" = "홍길동", "생일" = "413" 등으로 나타낼 수 있다.
딕셔너리란 말 그대로 사전이다.
딕셔너리는 key 와 value 를 한쌍으로 가지는 자료형이다.
딕셔너리는 리스트나 튜플처럼 순차적으로 값을 구하지 않고
key를 통해 value를 찾는다.

딕셔너리의 기본 형태
{key1 : value1, key2 : value2, ...}

'''

dic = {"name": "gildong", "age" : 18, "email": "gildong@"}

print(dic["name"])

dic["address"] = "부산 진구"
print(dic)

dic["name"] = "gilseo"
print(dic["name"])
print(dic)

## 값 추가
dic["pw"] = 1234
dic["hobby"] = ['soccer', 'baseball']
dic[10] = 20
print(dic)

# del dic[1] 딕셔너리는 인덱스가 없다.
# print(dic)
del dic['age']
print(dic)

# key를 통해 value 찾기
print(dic['email'])
print(dic['hobby'][0])


dic[(1, 2)] = 10
print(dic)

# dic[[1, 3]] = 20
# print(dic)

'''
딕셔너리의 키 값으로는 변하지 않는(immutable)
값을 사용해야함.
튜플은 immutable 이고, 
리스트 mutable 값이다.
'''

## 딕셔너리 관련 함수들
# key 리스트 만들기
dic = {"name": "gildong", "age" : 18, "email": "gildong@"}
print(dic.keys())
# 리스트 형태로 보여주지만 리스트의 기능은 없다.
# 추가, 수정, 삭제등이 안된다.

print(list(dic.keys()))

dic2 = list(dic.keys())
dic2.append("hihi")
print(dic2)

# key, value 쌍 얻기
print(dic.items())

dic.clear()
print(dic)

dic = {"name": "gildong", "age" : 18, "email": "gildong@"}

print(dic.get("age"))
print(dic.get("address"))

''' 불 자료형 '''
a = True
b = "True"
c = False
print(a)
print(type(a))
print()
print(b)
print(type(b))
print(c)
print()
print(2 > 1)
print(1 < 2)

c = 10
print(c > 20) # 기준은 무조건 왼쪽!!!!
print(20 < c)
print(c == 10)














