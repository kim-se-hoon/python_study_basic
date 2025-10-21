'''
패키지
: 도트(.)를 사용하여 파이썬 모듈을 계층적(디렉터리 구조)
으로 관리 할 수 있게 해주는 도구
'''

import chapter8.chapter8_1.test1
chapter8.chapter8_1.test1.test1_print()

from chapter8.chapter8_2.test2 import *
test2_print()

''' 예외 처리 '''

# a = 4 / 0
# b = [1, 2, 3]
# print(b[3])
# print("예외 뒤")
# print("try-catch 전")
# try:
#     print("이상 무")
#     a = 4 / 0
#     b = [1, 2, 3]
#     print(b[3])
#     print("예외 뒤")
# except:
#     print("ZeroDivisionError")
# print("try-catch 후")

print("try-catch 전")
try:
    print("이상 무")
    # a = 4 / 0
    # b = [1, 2, 3]
    # print(b[3])
    raise TypeError
    print("예외 뒤")
except ZeroDivisionError:
    print("원하는 예외 잡기")
except IndexError as e:
    print(e)
    print("인덱스 에러 잡기")
except:
    print("나머지 모든 예외 잡기")
print("try-catch 후")









