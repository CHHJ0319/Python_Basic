r1 = range(5)
print(list(r1))
r2 = range(2,5)
print(list(r2))
r3 = range(0,10,2)
print(list(r3))
r4 = range(0,10+1,2)
print(list(r4))
print()

n = 10
#r5 = range(n/2) #Type Error
r6 = range(n//2)
r7 = range(int(n/2))
print()

#for반복문
for i in range(5) :
    print(i)
print()

#리스트와 범위 조합
list1 = [1, 2, 1, 2]
for i in range(len(list1)):
    print("{}번째 {}".format(i, list1[i]))
print()

#역반복문
for i in range(5, 0-1, -1) :
    print(i)
print()

#while 반복문 상태 기반
list2 = [1, 2, 1, 2]
value =2
while value in list2 :
    list2.remove(value)
print(list2)
print()

#while 반복문 시간 기반
import time
count = 0
target_time = time.time() + 5
while time.time() < target_time :
    count +=1
print("5초 동안 {}번 반복".format(count))
print()

print(min(34, 26, 74))
print(max(34, 26, 74))
print()

#구문 내부에 여러 줄 문자열 사용
string1 = (
    "여러 줄 "
    "문자열"
    "입니다"
) #튜플X(문자열이 쉼표로 연결되어 있지 않으므로)
print(string1)
print(type(string1))
print()

n = 2
if n%2 == 0 :
#    print("""\
#        입력한 문자열은 {}입니다.
#        {}는(은) 짝수 입니다.\
#        """.format(n, n))

#    print("""입력한 문자열은 {}입니다.
#{}는(은) 짝수 입니다.""".format(n, n))

#    print("입력한 문자열은 {}입니다. {}는(은) 짝수 입니다.".format(n, n))

#문자열의 join()함수 사용
#    print("\n".join([
#        "입력한 문자열은 {}입니다.",
#        "{}는(은) 짝수 입니다."
#    ]).format(n, n))

    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는(은) 짝수 입니다."
    ).format(n, n))

else :
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는(은) 홀수 입니다."
    ).format(n, n))
print()

#이터레이터
list4 = [1, 2, 3, 4, 5]
r_list4 = reversed(list4) 
#reversed() 함수의 리턴값이 이터레이터, 리스트를 복제하여 뒤집은 것 X
# 리스트를 복제하는 것보다 기존 리스트를 활용하는 것이 효율적
print(next(r_list4))
print(next(r_list4))
print(next(r_list4))
print(next(r_list4))
print(next(r_list4))