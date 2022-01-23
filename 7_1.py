#math모듈
from distutils.util import change_root
import math
from random import random
import re

base = 10
print(math.log(10, base))

print()

#random모듈
import random

print(random.randrange(10))

print()

#sys모듈
import sys

print(sys.argv)
print("---")
#컴퓨터 환경 관련 정보 출력
print(sys.getwindowsversion())
print("---")
print(sys.copyright)
print("---")
print(sys.version)
#프로그램 강제 종료
#sys.exit()

print()

#os모듈
import os
print("현재 운영체제: ", os.name)
print("현재 폴더: ", os.getcwd())
print("현재 폴더 내부의 요소: ", os.listdir())

with open("old.txt", "w") as file1:
    file1.write("7-1 파일")
os.rename("old.txt","new.txt") #파일 이름 변경
os.remove("new.txt") #파일 제거

os.system("dir")
#현재 폴더의 파일/폴더 출력
output1 = os.listdir(".")
print(output1)
#현재 폴더의 파일/폴더 구분
for path in output1:
    if os.path.isdir(path):
        print("폴더: ", path)
    else:
        print("파일: ", path)

print()

#datetime 모듈
import datetime
#현재 시각 출력
now = datetime.datetime.now()
dtime1 = now.strftime("%Y.%m.%d %H:%M%S")
dtime2 = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,
    now.month,\
    now.day,\
    now.hour,\
    now.minute,\
    now.second)
dtime3 = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}".format(*"년월일시분초"))
print(dtime1)
print(dtime2)
print(dtime3)
print()
#특정 시간 이후의 시간 구하기
after = now + datetime.timedelta(\
    weeks=1,\
    days=1,\
    hours=1,\
    minutes=1,\
    seconds=1)
print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}".format(*"년월일시분초")))
print()
#특정 시간 요소 교체
change = now.replace(year=(now.year + 1))
print(change.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}".format(*"년월일시분초")))
print()

#time모듈
import time

print(time.time())
time.sleep(3)
print("3초간 정지했습니다.")
print()


#urllib모듈
from urllib import request

target = request.urlopen("https://www.google.co.kr/")
output2 = target.read()
print(output2)