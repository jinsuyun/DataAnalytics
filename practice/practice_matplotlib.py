import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# x=np.linspace(-np.pi,np.pi,100)
#
# c=np.cos(x)
# s=np.sin(x)
#
# plt.plot(x,c,'r*') # r은 빨간색 *은 표시
# plt.plot(x,s,'bo') # b는 파란색 o는 표시
#
# plt.show()

x=np.linspace(-np.pi,np.pi,100)
rand_array=np.random.randn(2,1000) #2행 1000열
uni_array=np.random.randn(2,1000)*6-3

plt.plot(rand_array[0],rand_array[1],'ro')
plt.plot(uni_array[0],uni_array[1],'g.')
# plt.show() # 출력 보여줌

data=np.loadtxt('../baseball_data.txt',delimiter=',')

data[data < 0 ] = 0 #0보다 작은 값은 0으로 만들기
data = data[data[:,1]>0] #홈런을 1개이상이라도 친 사람만 남겨라

h,hr,bb,k,sb,avg=data.T #행렬을 트랜스포즈 한 후 데이터를 넣어줌

hr_per_h = hr/h
bb_per_h=bb/h
k_per_h=k/h

hr_per_h/=np.max(hr_per_h)
bb_per_h/=np.max(bb_per_h)
k_per_h/=np.max(k_per_h)

plt.plot(hr_per_h,k_per_h,'rx')
plt.plot(hr_per_h,bb_per_h,'b.')
plt.show()



