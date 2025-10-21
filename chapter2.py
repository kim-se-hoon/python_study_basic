'''
리스트: 여러개의 값을 담을 수 있는 공간이다.
        -> 대괄호([])로 감싸 주고 각 요솟값을 쉼표(,)로 구분
'''

a = [1, 2, 3]
print(a)

b = []
print(b)

c = ["hello", "hi", "hihi"]
print(c)

d = [12, "hi", "apple", 24]
print(d)

e = [["apple", "banana"], [1000, 1500]]
print(e)

f = [["apple", 1000], ["banana", 1500]]
print(f)

''' 리스트의 인덱싱과 슬라이싱 '''
a = [1, 2, 3]
print(a[0])
print(a[2])

print(a[0] + a[2])
print(a[-1])

f = [["apple", 1000], ["banana", 1500]]
print(f[0][1])

kk = [["apple", 1000], ["banana", 1500], ['mango', 2000, ['3세이하 알레르기 조심', 'cc 알레르기 조심']]]

print(kk[2][2][0])
print(kk[2][2][1])

# 슬라이싱
a = [1, 2, 3, 3, 3, 3]
print(a[0:3])
print(a[0:3][0])

# 연산하기
a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)
print(a[0] + b[1])

print(a * 3)

# 수정과 삭제
a = [1, 2, 3]
a[2] = 4
print(a)

del a[1]
print(a)

a = [1, 2, 3, 4, 5, 6, 7, 8]
del a[1: 4]
print(a)

''' 리스트 관련 함수들 '''
# 리스트 요소추가
a = [1, 2, 3]
a.append(8)
print(a)
a.append("hihi")
print(a)
a.append([2, 3, 4])
print(a)

# 정렬
a = [1, 5, 2, 7, 3]
print(a)
a.sort()
print(a)
# 최저가순
b = ['k', 'c', 'f', 'e', 'o']
b.sort()
print(b)

a.reverse()
print(a)

## 인덱스 반환
a = [1, 2, 3]
print(a.index(3))

b = ['a', 'b', 'c', 'd']
print(b.index('c'))

## 리스트에 요소 삽입
a = [1, 2, 3, 4, 5]
a.insert(1, 11);
print(a)

## 리스트 요소 제거
a = ['k', 't', 'y', 'u']
a.remove('t')
print(a)

a = ['k', 't', 'y', 'u', 't', 't', 't']
a.remove('t')
print(a)

# 요소 뽑아내기
a = [1, 2, 3]
print(a.pop(1)) # 요소를 반환하고 삭제시킴
print(a)

print(a[1])
print(a)
print()
print("test")
a = [1, 2, 3, 4, 5, 6]
print(a[1])
print(a)
kk = a[2: 4]
print(kk)
print(kk[0])
print(kk)
print(kk.pop(1))
print(kk)

print()
a = [1, 2, 3, 4, 5]
print(a.count(1))

b = ['a', 'a', 'b', 'c', 'a']
print(b.count('a'))

# 리스트 확장
a = [1, 2, 3]
a.extend([4, 5])
print(a)
a.append([4, 5])
print(a)











