import pandas as pd
df = pd.read_csv('adult.data', header=None)
# data basic
print("SIZE")
print(df.size)
print("SHAPE")
print(df.shape) # 몇 x 몇 인지
print("BEFORE COLUMNS")
print(df.columns)
df.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation',
'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'wage']
print("AFTER COLUMNS")
print(df.columns)
print("DTYPES")
print(df.dtypes)
print("HEAD")
print(df.head())
print("TAIL")
print(df.tail())
# data summary
print("DESCRIBE")
print(df.describe()) #describe() - 각 attribute마다 요약한 정보를 제공
print("MEAN")
print(df.mean()) # mean() - 6개의 데이터에서 평균값(14개의 데이터 중 numerical 데이터 6개)
print("MODE")
print(df.mode()) # mode() - 카테고리에 해당하는 데이터만 mode
# Details
print("EDUCATION UNIQUE")
print(df.education.unique()) # 컬럼이름 education에 해당하는 모든 값
print("EDUCATION VALUE COUNT")
print(df.education.value_counts()) # 값에 대한 카운트
print("WAGE VALUE COUNT")
print(df['wage'].value_counts())
print("WAGE AGE MEAN")
print(df.groupby(['wage'])['age'].mean()) # age의 평균값
print("WAGE AGE STD")
print(df.groupby(['wage'])['age'].std()) # age의 std값
print("CAPITAL GAIN CORR AGE")
print(df['capital-gain'].corr(df['age']))