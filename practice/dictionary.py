import matplotlib.pyplot as plt
from wordcloud import WordCloud
test_dict=dict(d=4,a=1,b=2,c=4)
print(test_dict)
print(test_dict.keys())
print(test_dict.values())
print(test_dict.items())
for key in test_dict.keys():
    print(key,test_dict[key])

for key,value in test_dict.items():
    print(key,value)


#해당 txt파일에서 단어가 나오는 횟수 카운트하고 10개 이상인 단어 기준으로 오름차순으로 출력
lines=open('example.txt','r').readlines()
lines=[line.strip() for line in lines]
temp_list = []
for line in lines:
    temp_list.append(line.strip())
lines = temp_list

words_dict={}
for sentence in lines:#문장을 받아옴
    for word in sentence.split(" "):#split을 통해 단어를 받아옴
        if word in words_dict:#단어가 words_dict안에 있으면 카운트
            words_dict[word]+=1
        else:#단어가 없으면 1
            words_dict[word]=1

print(words_dict)

for i in sorted(words_dict.keys()):#words_dict를 키(단어)별로 정렬하고 그 값이 10이상이면 key(i)와 value(words_dct[i]를 출력
    if words_dict[i]>=10:
        print(i,words_dict[i])


lines=open('../example.txt').read()
wordcloud=WordCloud().generate(lines)
plt.figure(figsize=(12,12))
plt.imshow(wordcloud,interpolation='bilinear')
#plt.show("off")
plt.show()
