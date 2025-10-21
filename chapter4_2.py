''' for 문'''
test_list = ['one', 'two', 'three']
print("for 전")
for i in test_list:
    print(i)

print("for 후")
print()

marks = [60, 45, 88, 76, 79]
for i in marks:
    if i > 60:
        print(i, '점 입니다.')
        print("축하합니다. 합격입니다.")
    else:
        print(i, '점 입니다.')
        print("불합격입니다.")

print()
for i in range(1, 11):
    print(i)
print()
for i in range(7):
    print(i)

'''
구구단: 3
3 x 1 = 3
3 x 2 = 6
...
3 x 9 = 27
'''

dan = int(input("구구단: "))
for i in range(9):
    print(dan, 'x', (i + 1), '=', (dan * (i + 1)))













