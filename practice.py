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

# 사전
cabinet = {3:"유재석",100:"김태호"}
print(cabinet[3])
print(cabinet[100])

#추가
cabinet[7]="이윤식"

print(cabinet)
#print(cabinet[5]) 없으면 오류
print(cabinet.get(5)) #없어도 오류 안남
print(cabinet.get(5,"사용가능"))

print(3 in cabinet)
print(5 in cabinet)

#삭제
del cabinet[3]

print(cabinet)

#키들만 출력
print(cabinet.keys())

#value만 출력
print(cabinet.values())

#key,value 쌍으로 출력
print(cabinet.items())

#전체삭제
cabinet.clear()
print(cabinet)


#튜플 속도가 리스트보다 빠름
menu = ("돈까스","치즈까스")
print(menu[0])
print(menu[1])

#menu.add 사용불가

# name = "김종국"
# age= 20
# hobby = "코딩"
# print(name,age,hobby)

(name,age,hobby) = ("김종국",20,"코딩")
print(name,age,hobby)


#집합 (set)
#중복 안됨 , 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
py= set(["유재석","박명수"])

#교집합 (java와 py을 모두 할 수 있는 개발자)
print(java & py)
print(java.intersection(py))

#합집합 (java 할 수 있거나 py 할 수 있는 개발자)
print(java | py)
print(java.union(py))

#차집합 (java 할 수 있지만 py 은 할줄 모르는 개발자)
print(java - py)
print(java.difference(py))

#py 할 줄 아는 사람이 늘어남
py.add("김태호")
print(py)

#java를 까먹음
java.remove("김태호")
print(java)

#자료구조의 변경
menu1 = {"커피","우유","주스"}
print(menu1)
print(menu1, type(menu1))

menu1 = list(menu1)
print(menu1,type(menu1))

menu1 = tuple(menu1)
print(menu1, type(menu1))

menu1 = set(menu1)
print(menu , type(menu1))


#랜덤2
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst,1))

users = range(1,21) #1부터 20까지 숫자를 생성
#print(type(users))
users = list(users)
#print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users,4)
print("당첨자 발표")
print("치킨당첨자 : {0}".format(winners[0]))
print("커피당첨자 : {0}".format(winners[1:]))
print("축하합니다")

#if
#weather = "ㅁ"
weather = input("오늘 날씨는 어떄요?")
if(weather) == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

temp = int(input("기온은 어떄요?"))
if 30<=temp:
    print("너무 더워요. 나가지 마세요")
elif 10<+ temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0<= temp and temp <10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")


#for
for waiting_no in[0,1,2,3,4]:
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1,5): # 1,2,3,4
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨","토르","그루트"]
for customer in starbucks:
    print("{0},커피가 준비되었습니다".format(customer))

#while
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되엇습니다. {1} 번 남았어요".format(customer, index))
    index -=1
    if index ==0:
        print("커피는 폐기 처분되엇습니다")

# customer = "아이언맨"
# index = 1
# while True: #ctrl + c 강제종료
#     print("{0}, 커피가 준비 되엇습니다. 호출 {1} 회".format(customer, index))
#     index +=1

person = "Unknown"
while person != customer:
    print("{0}, 커피가 준비되었습니다".format(customer))
    person = input("이름이 어떻게 되세요?")

#continu break
absent = [2,5] #결석
no_book = [7] #책을 깜빡했음
for student in range(1,11): # 1,2,3,4,5,6,7,8,9,10
    if student in absent : 
        continue
    elif student in no_book:
        print("오늘 수업 여기싸지, {0}는 교무실로 다라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))

#한줄 for
#출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101,102,103,104
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print (students)

#학생 이름을 길이로 변환
students = ["iron man", "thor", "i am groot"]
students = [len(i) for i in students]
print(students)

#학생 이름을 대문자로 변환
students = ["iron man", "thor", "i am groot"]
students = [i.upper() for i in students]
print(students)

    









