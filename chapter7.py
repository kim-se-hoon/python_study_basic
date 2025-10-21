'''
모듈: 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일
      .py로 만든 파이썬 파일은 모두 모듈이다.

'''

# import chapter7_1
# print(chapter7_1.add(3, 4))
# print(chapter7_1.mul(3, 4))

# from chapter7_1 import add, mul
# from chapter7_1 import *
# print(add(5, 6))
# print(mul(10, 10))

'''
<모듈 불러오기 기본구조>
- import 모듈이름
  모듈이름.모듈 내 함수()
  
- from 모듈이름 import 모듈 함수1, 모듈 함수2
  모듈 내 함수()
 * 전체를 불러오고 싶으면 *을 사용
'''
import chapter7_1
print(chapter7_1.add(2, 3))

print(chapter7_1.num)

ch7 = chapter7_1.Hihi()
print(ch7.hihi2(10))





