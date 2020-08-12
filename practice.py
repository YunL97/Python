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



