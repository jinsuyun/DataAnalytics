'''다음의 값들을 아이템으로 갖는 두 리스트 객체를 생성함

10, 20, 30, 40, 30, 20, 10

100 이하 0 이상의 모든 짝수 정수

두 객체를 집합 자료형으로 변환하여 합집합 , 교집합 객체를 구하고 , 각각을 오름차순 정렬로 출력할 것'''

a=[10,20,30,40,30,20,10]
b=list(range(0,101,2))

set_a=set(a)#set으로 변환
set_b=set(b)

print("set으로 변환")
print(set_a)
print(set_b)

print("합집합")
print(set_a.union(set_b))
print("교집합")
print(set_a.intersection(set_b))#교집합

print("오름차순으로 정렬")
print(list(set_a))
print(sorted((set_a)))#sorted는 원본은 그대로 냅둠
print(set_a)
