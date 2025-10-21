import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
path = 'C:/data_Python'

df_exam = pd.read_excel(path + '/' +'excel_exam.xlsx')
# print(df_exam)
# print(df_exam['math'])

df_exam_novar = pd.read_excel(path + '/' +'excel_exam_novar.xlsx', header=None)
# print(df_exam_novar)

# df_exam = pd.read_excel(path + '/' +'excel_exam.xlsx', sheet_name=1)
# print(df_exam)

# df_exam = pd.read_excel(path + '/' +'excel_exam.xlsx', sheet_name="Sheet2")
# print(df_exam)
'''
sheet_name 에 숫자형 자료형을 넣으면 시트번호에 따라 들고옴
* 시트번호는 0번 인덱스부터 시작임
문자형 자료형으로 작성하면 이름에 맞게 들고옴


'''
df_csv_exam = pd.read_csv(path + '/' + "exam.csv")
# print(df_csv_exam)


df = pd.DataFrame({"name": ['홍길동', '홍길서', '홍길남', '홍길북'],
                   'english': [90, 80, 60, 70],
                   'math': [50, 60, 35, 20]})
df.to_csv('output_data.csv')
df.to_csv('output_data2.csv', index=False)

''' 데이터 파악하기 '''
'''
자주 쓰는 함수 정리
head(): 앞부분 출력
tail(): 뒷부분 출력
shape: 행, 열 갯수 출력
info(): 변수 속성
describe(): 요약 통계량
'''

path = 'C:/data_Python/'
exam = pd.read_csv(path + 'exam.csv')
# print(exam)

# print(exam.head())
# print(exam.head(10))
# print(exam.tail())

# print(exam.tail(7))
# print(exam.shape)
# print(exam.info())
# print(exam.describe())

'''
mpg 데이터 들고오고
출력해보기
요약통계량 출력하기
'''
mpg = pd.read_csv(path + 'mpg.csv')
# print(mpg)
# print(mpg.info)
# print(mpg.describe())

'''
manufacturer: 제조사
model: 모델명
displ: 배기량
year: 생산연도
cyl: 실린더 갯수
trans: 변속기
drv: 구동방식(f가 프론트임)
cty: 도심연비
hwy: 고속도로 연비
fl: 연료 종류
category: 자동차 종류
'''

# 파생변수 만들기
# print(mpg)
# print()
mpg['total'] = (mpg['cty'] + mpg['hwy'])
# print(mpg)
'''
1. 새로운 파생변수를 만들어 
   각각의 평균연비를 구하시오(total_mean)
   
2. 모든 데이터의 전체 평균 연비를 구하시오
   출력: 36
'''
mpg['total_mean'] = (mpg['cty'] + mpg['hwy']) / 2
# print(mpg)
# print(sum(mpg['total_mean']) / len(mpg))
# print(mpg['cty'])
# print(mpg['hwy'])
# mpg['total'].plot.hist()
# plt.show()

mpg['test'] = np.where(mpg['total'] >= 40, "pass", "fail")
# print(mpg['test'].value_counts())
#
# count_test = mpg['test'].value_counts()
# count_test.plot.bar(rot = 0)
# plt.show()

mpg['grade'] = np.where(mpg['total'] >= 50 , "A",
                        np.where(mpg['total'] >= 40, "B", "C"))

'''
A, B, C 등급 갯수 확인
그래프 출력
'''
print()
print(mpg['grade'].value_counts())

# count_test = mpg['grade'].value_counts().sort_index()
# count_test.plot.bar(rot = 0)
# plt.show()
print(mpg['category'].value_counts())
'''
numpy
AND -> &
OR -> |
'''
'''
실습
size라는 새로운 파생변수를 만드시오
size는 카테고리에 따라 새로 지정됩니다
카테고리가 compact, subcompact -> s
midsize, 2seater -> m
나머지는 -> l

카테고리 항목에대해 갯수를 출력하고
그래프로도 표현하시오
'''
print()
mpg['size'] = np.where((mpg['category'] == "compact") | (mpg['category'] == "subcompact"), "s",
                       np.where((mpg['category'] == "midsize") | (mpg['category'] == "2seater"), "m", "l"))
# print(mpg['size'].value_counts())
# count_test = mpg['size'].sort_values().value_counts()
# count_test.plot.bar(rot = 0)
# plt.show()
mpg['size'] = np.where(mpg['category'].isin(['compact', 'subcompact']), 's',
                       np.where(mpg['category'].isin(['midsize', '2seater']), "m", "l"))
# print(mpg['size'].value_counts())
# count_test = mpg['size'].sort_values().value_counts()
# count_test.plot.bar(rot = 0)
# plt.show()

''' 데이터 가공하기 '''
'''
1. 전처리 - 원하는 형태로 만드는 것
2. 조건에 맞는 데이터 추출
3. 필요한 변수만 추출
4. 순서 정렬
5. 파생변수 추가
6. 집단별 요약
7. 데이터 합치기
'''

'''
전처리에 자주 사용되는 판다스 함수
query(): 행 추출
df[]: 열(변수) 추출
sort_values: 정렬
groupby(): 집단별로 나누기
assign(): 변수 추가
agg(): 통계치 구하기
merge(): 데이터 합치기(열 기준)
concat(): 데이터 합치기(행 기준)
'''

exam = pd.read_csv(path + 'exam.csv')
# print(exam)
# print(exam.query('nclass == 1'))
# print(exam.query('nclass != 1'))
# print(exam.query('math > 50'))
# print(exam.query('english >= 70'))
# print(exam.query('math > 50 & english >= 70'))
# print(exam['math'].mean())
# print(exam[['math', 'english']])

'''
mpg
사이즈가 s, m 사이즈 중 total연비가 50이상인것의
제조사와 차종(모델명)을 나열하시오
'''
# print(mpg.query('total >= 50 & (size == "s" | size == "m")')[['manufacturer', 'model']])

# 오름차순
# print(exam.sort_values('math'))
# 내림차순
# print(exam.sort_values('math', ascending=False))

# print(exam.sort_values(['nclass', 'math'], ascending=[False, True]))

# 파생변수(함수로 만들기)
# print(exam.assign(total = exam['math'] + exam['english'] + exam['science']))

'''
mean 이라는 학생들의 3과목 평균점수 파생변수를 만드시오
그리고 평균 점수를 내림차순으로 정렬하여 id와 mean을 출력하십시오
'''
# print(exam.assign(mean = (exam['math'] + exam['english'] + exam['science']) / 3)
#             .sort_values('mean', ascending=False)[['id', 'mean']])

'''
반별로 세과목의 평균 점수의 평균을 추출하여
1반 80
2반 79
...

위의 데이터를 새로운 데이터프레임을 만들어서 넣은 뒤
classMean.xlsx 파일로 저장하시오
'''
# print(exam.assign(mean = (exam['math'] + exam['english'] + exam['science']) / 3)
#             .sort_values('mean', ascending=False)[['id', 'mean']])

# print(exam.assign(mean = (exam['math'] + exam['english'] + exam['science']) / 3))
# print(exam)
exam2 = exam.assign(mean = (exam['math'] + exam['english'] + exam['science']) / 3)
# print(exam2)

print(exam2.query('nclass == 1'))
print(sum(exam2.query('nclass == 1')['mean']) / len(exam2.query('nclass == 1')['mean']))

exam2MeanNClass1 = sum(exam2.query('nclass == 1')['mean']) / len(exam2.query('nclass == 1')['mean'])
exam2MeanNClass2 = sum(exam2.query('nclass == 2')['mean']) / len(exam2.query('nclass == 2')['mean'])
exam2MeanNClass3 = sum(exam2.query('nclass == 3')['mean']) / len(exam2.query('nclass == 3')['mean'])
exam2MeanNClass4 = sum(exam2.query('nclass == 4')['mean']) / len(exam2.query('nclass == 4')['mean'])
exam2MeanNClass5 = sum(exam2.query('nclass == 5')['mean']) / len(exam2.query('nclass == 5')['mean'])

print(exam2MeanNClass1)
print(round(exam2MeanNClass2, 1))
print(round(exam2MeanNClass3, 1))
print(exam2MeanNClass4)
print(exam2MeanNClass5)

examClassMean = pd.DataFrame({"nclass": [1, 2, 3, 4, 5],
                   'mean': [round(exam2MeanNClass1, 1), round(exam2MeanNClass2, 1), round(exam2MeanNClass3, 1), round(exam2MeanNClass4, 1), round(exam2MeanNClass5, 1)]})

print()
print(examClassMean)
# examClassMean.to_csv('classMean.csv', index=False)

print("hi")
# 집단별로 요약하기
print(exam2.groupby('nclass').agg("mean", "mean")['mean'])

'''
agg 함수 속성 정리
1. mean: 평균
2. std: 표준편차
3. sum: 합계
4. median: 중앙값
5. max: 최댓값
6. min: 최솟값
7. count: 빈도(총갯수)
'''
print(exam.groupby('nclass').agg(mean_math = ("math", "std")))




