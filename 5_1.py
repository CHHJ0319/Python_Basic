def Function1(value1, *value2, value3="기본 매개변수"):
    print(value1)
    for val in value2:
        print(val)
    print(value3)

Function1("일반 매개변수","가변 매개변수1", "가변 매개변수2")
#일반 매개변수는 해당 위치에 반드시 입력, 일반적으로 일반 매개변수는 필수로 순서에 맞게 입력해야 함 
print()

#def Function2(value1="기본 매개변수1", value2):
#어떤 매개변수에 입력이 되는지 알 수 없음
def Function2(value1="기본 매개변수1"):
    print(value1)
Function2("기본 매개변수2")
print()

def Function3(value1="기본 매개변수1", *value2, value3="기본 매개변수2" ):
    print(value1)
    print(value2) #가변 매개변수가 우선
    print(value3)

Function3("가변 매개변수1", "가변 매개변수2", "기본 매개변수3",
          value3="키워드 매개변수")
print()

def Function4(value1, value2, value3="키워드 매개변수3", value4="키워드 매개변수4"):
    print(value1)
    print(value2)
    print(value3)
    print(value4)

Function4(value2="키워드 매개변수2", value1="키워드 매개변수1", value4="키워드 매개변수5")
print()

def Function5():
    print("리턴 전")
    return
    print("리턴 후")

Function5()
print()

#아무것도 리턴하지 않기
def Function6():
    return

result = Function6()
print(result)
print()

def Function7(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i
    return sum

print(Function7(1, 10))

def Function8(start, end):
    result = 1
    for i in range(start, end+1):
        result *= i
    return result

print(Function8(1, 10))
    
