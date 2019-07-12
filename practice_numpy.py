import numpy as np
#numpy에서 배열은 동일한 타입의 값들을 가지며, 배열의 차원을 rank 라 하고, 각 차원의 크기를 튜플로 표시하는 것을 shape 라 한다.
# 예를 들어, 행이 2이고 열이 3인 2차원 배열에서 rank는 2 이고, shape는 (2, 3) 이 된다.
list_var2=[0,1,'aa','bb']
arr_var2=np.array(list_var2)
print(list_var2)
print(arr_var2) # numpy는 리스트에 다른 타입을 넣는 것이 아닌 하나의 타입으로 들어간다. 0,1이 문자로 됨
print()

print(arr_var2.shape)# 몇x몇 행렬인지 알려줌
print(arr_var2.ndim) #ndim은 차원을 의미
print()

a=np.array([[1,5,7],[1,2,3]])
b=np.array([1,3,5,7,2,4,6,8,3,6,9,12])
print("a ndim",a.ndim," b ndim",b.ndim)
print("a shape",a.shape," b shape",b.shape)
print()

a=np.identity(5) #nxn짜리 단위행렬 생성
print(a)
print()

a=np.arange(10,20,2)
print(a)
a=np.linspace(0,1,11) #시작점과 끝점을 균일 간격으로 나눈 점들을 생성해주는 linspace()함수도 있다.
print(a)
print()

a_np=np.array([1,3,5])
print(a_np*a_np)
print()

#numpy array 는 mutable 이지만 , 일반적으로 연산 수행 혹은 메서드 실행 시 새로운 객체를 생성함
a=np.array([[1,2,3],[4,5,6]])
print("기본 array",a)
print()
b=a
a=a*2
print("a=a*2를함",a)
print()
print("b는 ",b)
print()
b=a
a*=2
print("a*=2를함",a)
print()
print("b는",b)
print()

a=np.array([[1,4,2,3,4,5],[2,5,6,5,2,1]])
b=np.array([1,2,3,4,5,6])
c=np.array([3.5,2.4])
d=np.ones_like(a)*2.2
result=3*a-d
result=c.dot(result)
print("result",result)
result=result.dot(b)#1x6 1x6행렬의 곱이지만 스칼라를 원한다고 생각하여 자동으로 reproduct를 하고 스칼라값을 도출한다.
print("result",result)
print()

#모든 원소를 0으로 채우는 zeros, 1로 채우는 ones, 그리고 단위 행렬을 만들어주는 eye
a=np.zeros((2,2))
print("zero",a)
a=np.ones((2,2))
print("ones",a)
a=np.ones_like(a)
print("ones_like",a)
a=np.eye(2)
print("eye",a)
print()

b=np.array([[1,3,5,7],[2,4,6,8],[3,6,9,12]])
print(b)
print(b[1,3])
print(b[0])
print(b[0,:])
print(b[:,2])
print(b[1:,::2])
print()

a=np.array([range(11,17),range(17,23),range(23,29),range(29,35)])
print(a[:2,3:])
print()
print(a[::2])
print()
print(a[:,4])
print()
print(a[:,1::3])
print()
print(a[::2,1::2])
print()

c=np.array([[1,2,3],[4,5,0]])
print((c==0).any()) #.any()는 하나라도 조건에 충족하는 값이 있는가 --> c안에 0이라는 값이 1개라도 있냐
print((c==0).all()) #.all()은 조건 안에 모든 값이 그러한가 --> 모든 값이 c==0을 만족하는가
print()

a=np.array([range(1,8,2),range(2,9,2),range(3,10,2)])
print(a)
print(a.reshape(6,2))#행렬을 다시 reshape해준다
print()

d=np.arange(11,35).reshape(4,6) #행렬을 만들때 편하게 만들수 있음 arange로 범위를 정하고 reshape로 몇x몇 행렬인지 정함
print(d)
e=np.arange(24).reshape(4,6)
f=np.arange(24).reshape(4,6)
print(np.concatenate((d,e)))#괄호 치는게 중요 concatenate는 2개의 행렬을 합치는 것
print()

a=np.array([[2,4],[0,1]])
b=np.array([[1,1],[1,1]])
c=b/a
print(c)

check=np.isnan(c)
print(check)
#check=np.logical_or(np.isinf(c))
#print(check)

