import seaborn as sns
import matplotlib.pyplot as plt

# var = ['a', 'a', 'b', 'c']
# sns.countplot(x = var)
# plt.show()

df = sns.load_dataset('titanic')
# print(df)
# sns.countplot(data=df, x = 'class', hue='alive')
# plt.show()

# sns.countplot(data=df, y = 'class', hue='alive')
# plt.show()

import pandas as pd
df = pd.DataFrame({"name": ['홍길동', '홍길서', '홍길남', '홍길북'],
                   'english': [90, 80, 60, 70],
                   'math': [50, 60, 35, 20]})
# print(df)

# 만든 데이터로 분석하기
print(df['english'])
print()

# 변수값으로 합계 구하기
print(sum(df['english']))

# 변수값으로 평균 구하기
print(sum(df['english']) / len(df['english']))






