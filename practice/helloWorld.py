########################################################
print('Hello World!!!')
print('*' * 15)
print('Hello Python!!!')
print('*' * 15)
print('Hello PyCharm!!!')
print('*' * 15)

########################################################
a=range(10)#0~10까지 범위를 준다.
print(a)
result=[]
for num in a:
    result.append(num*10)
print(result)

result=[num*10 for num in range(10)]
print(result)

########################################################
count=0
while count <10:
    print(count)
    count+=1
    if count>5:
        break
print("*****************")
count=0
while count<10:
    count+=1
    if count % 2 == 0:
        continue
    print(count)

print("*******************")
########################################################

# name = input("Please enter a String: ")
# odd_seq =''
# even_seq=''
# for num in name[::2]:#[i:j:k]는 i부터 j까지 범위를 나타내며 k는 넘어가는 수를 나타낸다 k가 2라면 2칸씩 넘어감
#     odd_seq+=num+'='
# for num in name[1::2]:
#     even_seq+='='+num
#
# even_seq+='='*(len(odd_seq)-len(even_seq))
# border_line='-+'*(len(odd_seq)//2) # //는 나눈 것의 몫을 나타냄 %는 나머지를 나타냄
#
# print(border_line)
# print(odd_seq)
# print(even_seq)
# print(border_line)

# odd_seq=''.join([x+"=" for x in name[::2]])
# even_seq=''.join(["="+x for x in name[1::2]])
# even_seq+="="*(len(odd_seq)-len(even_seq))
# head_footer ="-+"*(len(odd_seq)/2)
#
# print("|"+head_footer+"|")
# print("|"+odd_seq+"|")
# print("|"+even_seq+"|")
# print("|"+head_footer+"|")
#################################################
input_list=[1,4,4,1]
result=False
reverse=list(reversed(input_list))#reversed는 배열을 거꾸로 해준다.
# if input_list==input_list[::-1]: #[::-1]은 배열을 거꾸로 해주는 것
#     result=True
if input_list==reverse:
    result = True
print(result)
#append는 통째로 list에 집어넣는 것
#extend는 하나하나 쪼개서 뒤에 element로 추가
#+는 그냥 list를 더하는 것. 반환 값을 만들어야 한다.

#파이선은 리턴값을 여러개 줄 수 있다. 여러개의 값을 리턴 할 때는 튜플--> immutable

################################################
def sort_to_num(num1,num2):#함수 정의
    if num1>num2:
        return num1, num2
    else:
        return num2, num1


res=sort_to_num(1,3)#함수 선언
print(res[0],res[1])

#################################################
num=2
print(num)
def local_num():
    num=1 #전역변수 num과 다른 변수임

local_num()
print(num) #전역변수를 함수 안에서 값을 바꿔도 값이 변하지 않는다

###################################################
#파이선은 Pass by value, Pass by reference 둘다 아니고 굳이 따지면 Pass by object reference에 가깝다
#그 이유는 object의 mutable/immutable 여부에 따라 결과값이 달라질 수 있기 때문

def repair_list(test_list):
    assert isinstance(test_list,list)
    test_list.append(0)
    test_list.append(-1)

temp_list=[1,2,3,4,5]
print(temp_list)
repair_list(temp_list)
print(temp_list)

###################################################

#파라미터 변수에 디폴트 값을 주려면 하나만 주지 못하고 나머지 전부 주어야한다. 하나만 주려면 마지막에 넣어야한다.
#즉, 처음 변수에 디폴트 값을 명시 못함
def check(a,b,c=10):
    return

###################################################


###################################################
###################################################
###################################################
###################################################





