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


#함수
def open_account():
    print("새로운 계좌가 생성되었습니다")


open_account()

def deposit(balance, money): #입금
    print("입금이 완료되었습니다. 잔액은 {0}원입니다".format(balance + money))
    return balance + money

def withdraw(balance,money): #출금
    if balance >= money: #잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다".format(balance-money))
        return balance - money
    else:
        print("출금이 완료되지않았습니다.잔액은 {0}원입니다".format(balance))
        return balance

def withdraw_night(balance,money): #저녁에 출금
    commission = 100 #수수료 100원
    return commission,balance - money-commission
balance = 0
balance = deposit(balance,2000)
print(balance)
balance = withdraw(balance,2000)
commission, balance = withdraw_night(balance,500)
print("수수료 {0}원이며, 잔액은 {1}원 입니다".format(commission,balance))

# def profile(name, age=17, main_lang="파이썬"):
#     print("이름: {0}\t나이 : {1}\t주 사용 언어:{2}"\
#         .format(name,age,main_lang))
# profile("유재석")

#가변인자
def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name,age),end=" ") #end=" " 줄바꿈x
    #print(lang1,lang2,lang3,lang4,lang5)
    for lang in language:
        print(lang, end=" ")
    print()


profile("유재석",20,"파이선","자바","c","c++","c#")
profile("김태호",25,"코틀린","스위프트","","","")

#지역변수와 전역변수

gun = 10

def checkpoint(soliders): #경계근무
    global gun # 전역공간에 있는 gun 사용
    #gun=20
    gun = gun-soliders
    print("[함수내]남은 총: {0}".format(gun))

def checkpoint_ret(gun,soldiers):
    gun = gun-soldiers
    print("[함수 내]남은 총: {0}".format(gun))
    return gun

print("전체 총: {0}".format(gun))
checkpoint(2) #두명이 경계근무 나감
gun= checkpoint_ret(gun,2)
print("남은 총: {0}".format(gun))

#표준 입출력
print("python", "java")
print("python","java",sep=" vs ", end="?")
print("무엇이 더 재미있을까요?")

import sys
print("python","java",file=sys.stdout)
print("python","java",file=sys.stderr)

#시험성적
#정렬
scores = {"수학":0, "영어":50,"코딩":100}
for subject,score in scores.items():
    #print(subject,score)
    print(subject.ljust(8),str(score).rjust(4),sep=":")

#은행 대기순번표
# 001, 002 ,002 ,...
for num in range(1,21):
    print("대기번호 : " +str(num).zfill(3))

answer = input("아무  값이나 입력하세요 : ") #사용자입력은 항상 문자열로 입력
print(type(answer))
# print("입력하신 값은 "+answer + "입니다")

#다양한 출력 포멧
#빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
#양수일땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
#왼쪽 정렬하고, 빈칸으로 _채움
print("{0:_<+10}".format(-500))
# 3자리마다 콤마를 찍어주기
print("{0:,}".format(100000000000))
# 3자리마다 콤마를 찍어주기. +-부호도 붙이기
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))
#3자리마다 콤마를 찍어주는데, 부호도 붙이고, 자릿수고 확보하기
# 빈자리는 ^표시로 채워주기
print("{0:^<+30,}".format(100000000000))
#소수점 출력
print("{0:f}".format(5/3))
#소수점 특정 자리수 까지만 표시(소수점 3째 자리에서 반올림)
print("{0:.2f}".format(5/3))

#파일 입출력
# score_file = open("score.txt","w",encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

#a 이어서씌우기
# score_file = open("score.txt","a",encoding="utf8")
# score_file.write("과학은 :80")
# score_file.write("\n코딩 : 100")
# score_file.close()

#읽기
# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.read())
# score_file.close()

score_file = open("score.txt","r",encoding="utf8")
print(score_file.readline())#줄별로 읽기, 한줄 읽고 커서는 다음줄로 이동
print(score_file.readline())
score_file.close()
# while True:
#     line score_file.readline()
#     if not lint:
#         break
#     print(lint)
# score_file.close()
score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readlines() #리스트 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()

#pickle 프로그램상에서 사용하고 있는 데이터를 파일형태로 저장
import pickle
# profile_file = open("profile.pickle","wb")
# profile = {"이름":"박명수","나이":30,"취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile,profile_file) #profile에 있는 정보를 file에 저장
# profile_file.close

profile_file = open("profile.pickle","rb")
profile = pickle.load(profile_file) #file에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()

#with 조금더 편하게 위와 동일한 작업 가능 다끝나면 close도 됨
with open("profile.pickle","rb") as profile_file:
    print(pickle.load(profile_file))

# with open("study.txt","w",encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())

#클래스

#마린 : 공격 유닛, 군인. 총을 쏠수 있음
name = "마린" #유닛의 이름
hp = 40 #유닛의 체력
damage = 5 #유닛의 공격력

print("{0} 유닛이 생성되었습니다".format(name))
print("체력{0} 공격력{1} ".format(hp,damage))

#탱크 : 공격유닛, 탱크, 포를쏠 수 있는데, 일반모드/ 시즈모드
tank_name="탱크"
tank_hp = 150
tank_damage = 35
print("{0} 유닛이 생성되었습니다".format(tank_name))
print("체력{0} 공격력{1} ".format(tank_hp,tank_damage))

def attack(name,location,damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]".format(\
        name,location,damage))

attack(name,"1시",damage)
attack(tank_name,"1시",tank_damage)

#일반 유닉
class Unit:
    def __init__(self, name, hp, speed): 
        self.name = name
        self.hp=hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1}의 방향으로 이동합니다.[속도 {2}]"\
            .format(self.name, location, self.speed))

#메딕: 공격력 0일떄 어케하냐

# marine1 = Unit("마린",40,5)
# marine2 = Unit("마린",40,5)
# tank = Unit("탱크",150,35)

#레이스 :공중 유닛, 비행기. 클로킹(상대방에게 보이지 않음)
# wraith1 = Unit("빼앗은레이스",80,5)
# print("유닛이름 :{0},공격력 : {1}".format(wraith1.name,wraith1.damage))

# #마인드 컨트롤 :상대방 유닛을 내것으로 만드는것 (빼앗음)
# wraith2 = Unit("레이스",80,5)
# wraith2.clocking = True
# if wraith2.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다".format(wraith2.name))


#공격 유닛
class AttackUnit(Unit): # 상속
    def __init__(self, name, hp, speed,damage): 
        Unit.__init__(self,name,hp, speed)

        self.damage = damage

    def attack(self,location):
        print("{0}:{1}방향으로 적군을 공격합니다.[공격력{2}]"\
            .format(self.name,location,self.damage))

    def damaged(self,damage):
        print("{0} : {1}데미지를 입었습니다.".format(self.name,damage))
        self.hp -= damage
        print("{0}:현재 체력은 {1} 입니다".format(self.name,self.hp))
        if self.hp <=0:
            print("{0} :파괴되었습니다.".format(self.name))

# #파이어뱃 : 공격 유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃",50,16)
# firebat1.attack("5시")

# #공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

#드랍쉽 : 공중 유닛, 수송기. 마린/ 파이어뱃/ 탱크등을 수송. 공격x

#날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
            print("{0} : {1} 방향으로 날아갑니다. [속도{2}]"\
                .format(name, location, self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp,damage, flying_speed):
        AttackUnit.__init__(self, name,hp,0, damage) #지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# #발키리: 공중 공격 유닛, 한번에 14발 미사일 발사.
# valkyrie = FlyableAttackUnit("발키리",200,6,5)
# valkyrie.fly(valkyrie.name, "3시")

#연산자 오버로딩

# 벌쳐: 지상유닛, 기동성이 좋음
valture = AttackUnit("벌쳐", 80, 10,20)

#배틀 크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀 크루저", 500, 25, 3)

valture.move("11시")
#battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")

#pass
#건물
#super
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         #Unit.__init__(self, name, hp, 0)
#         super().__init__( name, hp, 0)
#         self.location= location

#서플라이 디폿: 건물, 1 개 건물 = 8 유닛.
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다")

# def game_over():
#     pass

# game_start()
# game_over()


#예외처리
try: 

    print("나누기 전용 계산기 입니다")
    nums=[]
    nums.append(int(input("첫번째 숫자를 입력하세요: ")))
    nums.append(int(input("두번째 숫자를 입력하세요: ")))
    #nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))

except ValueError:
    print("에러 발생")

except ZeroDivisionError as err:
    print(err)

except Exception as err:
    print("알 수 없는 오류")
    print(err)

#사용자 정의 예외처리
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

#에러 발생시키기
try:
    print("한자리 숫자 나누기 전용 계산기입니다")
    num1 = int(input("첫번째 숫자 입력"))
    num2 = int(input("두번째 숫자 입력"))
    if(num1>=10 or num2>=10):
        #raise ValueError #해당 예외 처리하는곳으로 보내는것
        raise BigNumberError("입력값: {0}, {1}".format(num1,num2))
    print("{0}/{1} = {2}".format(num1,num2,int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력, 한자리 숫자만 입력하세요")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한자리 숫자만 입력")
    print(err)
finally:
    print("계산기를 이용해주셔서 감사합니다")

#모듈
# import module 
# module.price(3) #3명에서 영화보러 갔을때 가격
# module.price_morning(4)
# module.price_soldier(5)

# import module as mv # 별명 가능
# mv.price(3) #3명에서 영화보러 갔을때 가격
# mv.price_morning(4)
# mv.price_soldier(5)

# from module import * # 함수 바로 호출 가능
# price(3) #3명에서 영화보러 갔을때 가격
# price_morning(4)
# price_soldier(5)

from module import price, price_morning #가져다 쓸것만 할당 가능
price(5)

#패키지
import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()






