import numpy as np
import pandas as pd

# data = pd.Series([0.25, 0.5, 0.75, 1.0])
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
# print(data)
# print(data.index)
# print(data[['b', 'c']])


# A = pd.DataFrame(np.random.randint(0, 20,(2, 2)),
#                  columns=list('AB'))
#
# print(A)
#
# B = pd.DataFrame(np.random.randint(0, 10, (3, 3)),
#                  columns=list('BAC'))
#
# B.fillna()

area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
                   'Florida': 170312, 'Illinois': 149995}
area = pd.Series(area_dict)
# print(area['California': 'Illinois'])
#
population_dict = {'California': 38332521, 'Texas': 26448193, 'New York': 19651127,
                           'Florida': 19552860, 'Illinois': 12882135}
population = pd.Series(population_dict)
#
# # print(area.index)
# # print(population)
# #
states = pd.DataFrame({'population': population, 'area': area})
# print(states)
# print(states.values)
# print(states.index)
# print(states.columns)

# print(states['area']['Texas'])
# print(states['population'])

print(states)
states['density'] = states['population'] / states['area']
print("STATES에 density를 추가함")
print(states)
print("STATES의 조건 density 값이 100보다 큰 것 TRUE FALSE")
print(states['density']>100) # False/True로 생성됨
print("California라는 키값에 관한 정보를 불러옴")
print(states.loc['California'])

print("전체 정보 loc를 통한 데이터 수정 전")
print(states)

states.loc[states.density > 100, ['density']] = 10 #density의 컬럼에서 100보다 큰 값을 10으로 바꾼다는 뜻
print("loc 를 통한 데이터 수정 후")
print(states)
print("states의 평균")
print(states.mean())

# states.loc[states.density > 100, ['density']] = 10
#
print("states의 합")
print(states.sum())

A = pd.DataFrame([{'A': 17, 'B': 3}, {'A': 17, 'B': 11}])
B = pd.DataFrame([{'B': 0, 'A': 1, 'C': 2}, {'B': 5, 'A': 8, 'C': 7}, {'B': 3, 'A': 0, 'C': 3}])

print("A")
print(A)
print("B")
print(B)
print("A-2")
print(A-2)
print("A의 1행")
print(A.iloc[0])

print("B")
print(B)
print("A+B") #행렬이 겹치는 부분만 계산
print(A+B)
'''
DataFrame 에서는 결측치 (missing 를 처리하기 위한 다양한 함수를 지원

isnull (): 각 element 에 대해 null 여부를 검사한 뒤 masking DataFrame 생성

dropna (): nan 을 포함하는 열이나 행이 있을 경우 해당 열 행을 삭제한 DataFrame 을 반환

axis=0 : 행 단위로 검사하며 1 일 경우 열 단위로 검사함

how=‘any’ : 하나라도 nan 이 존재할 경우 해당 행 열을 삭제 .
‘all 로 설정되어 있을 경우에는 해당 열 행의 모든 데이터가 nan 이어야만 삭제

fillna (): nan 값을 주어진 값으로 모두 변경함

dropna () 및 fillna 함수는 새로운 객체를 생성하게 되므로 원래 객체는 변경되지 않음

원래 객체에 반영되길 원하면 각 함수 파라미터 중 inplace = True 로 설정
'''
df = pd.read_csv('../sample_iris.csv') # csv데이터 읽어오기
print("데이터크기 \n",df.size) # 데이터 크기
df = df.fillna('aaaaa') # Missing Value를 다른 값으로 채워준다.
print(df)

# df = df.dropna(how='all')
# df = df.dropna()
# print(df.size)


# print(df)
# df = df.fillna(value='aaaaa')
# print(df)


