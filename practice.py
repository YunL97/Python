print(1, "풍선")
print(str(1)+"풍선")
print(not( 5 > 10))

print(2**3) # 2^3
print(5//3) # 몫

print((3>0) or (3>5)) #True
print((3>0) | (3>5))#True

print(5>4>3)#True
print(5>4>7)#False

print(abs(-5)) #5
print(pow(4,2))#16
print(max(5,12)) #12
print(min(5,12)) #5

from math import *
from random import *
print(floor(4.99)) # 내림 4
print(ceil(3.14)) #올림 4
print(sqrt(16)) #제곱근4

print(random())
print(randrange(1,46)) # 1-46
print(randint(1,45)) # 2-45

sent = """
aasd
asd
asd
"""
print(sent)

jum = "970502-1234567"

print("성별" + jum[7])
print("연" + jum[0:2]) # 0부터 2 직전까지 97
print("월" + jum[2:4])
print("일" + jum[4:6])
print("생년월일" + jum[0:6]) #처음부터 6 직전까지
print("뒤 7자리" + jum[7:]) # 7부터 끝까지
print("뒤 7자리 (뒤에서부터) : " + jum[-7:])# 맨뒤에서 7번째부터 끝까지

python = "Python is Amazing"
print(python.lower())
print(python.upper)
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n")
print(index)
index = python.index("n",index+1)
print(index)

print(python.find("Java"))
#print(python.index("Java"))

print("나 %d 살입니다" %20)
print("sksms %s을 좋아해요" %"파이썬")
print("Apple은 %c로 시작해요" %"A")
print("나는 %s 색과 %s 색을 좋아해요" %("파란","빨간"))
print("나는 {}살입니다".format(20))
print("나는 {0}색과 {1}색을 좋아해요".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간"))
print("나는 {age}살이며, {color}색을 좋아해요".format(age=20,color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요".format(color="빨간",age=20))

age= 20
color= "빨간"
print(f"나는 {age}살이며, \n{color}색을 좋아해요")

print("저는 '이윤식'입니다")
print('저는 "이윤식"입니다')
print("저는 \"이윤식\"입니다")

# \\: 문장 내에서 \
print("저는 '이윤식'입니다")
print("C:\\Users\\lee\\Desktop\\Python")

#\r 커서를 맨앞으로 이동
print("Red Apple \rPine")

# \b :백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t: 탭
print("Red\tApple")

# 리스트[]
subway = [10,20,30]

print(subway)

subway = ["유재석","조세호","박명수"]

#조세호씨가 몇번째 칸에 있는가
print(subway.index("조세호"))

#하하가 다음정류장에서 다음칸에 탐
subway.append("하하")
print(subway)

#정형돈 유재석, 조세호 사이
subway.insert(1,"정형돈")
print(subway)

#지하철에있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

#print(subway.pop())
#print(subway)

#print(subway.pop())
#print(subway)

#같은 이름의 사람이 몇명인지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

#순서 뒤집기
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형 함꼐 사용
mix_list = ["조세호",20,True]
print(mix_list)

#리스트 확장
num_list.extend(mix_list)
print(num_list)






