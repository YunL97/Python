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
print("생년월일" + jum[0:6])
print("뒤 7자리" + jum[7:])


