print("문자열1",'문자열2')
#print(""문자열3"") #Syntax Error: 자료(문자열)와 자료(문자열)를 단순하게 나열 못 함
print("'문자열3'")
print()

#여러 줄 문자열
print("""여러 줄 문자열 입니다.
가나다라마바사아자차카타파하
ABCDEFGHIJKLMNOPQRSTUVWXYZ""") #''' '''도 가능
print("""\
줄바꿈을
하지 않고
출력\
""")
print()

print("문자열 "+"연결 연산자")
#print("문자열"+1) #Type Error: 문자열은 문자열끼리, 숫자는 숫자끼리
print("문자열 반복 연산자\t"*2)

#인덱싱 슬라이싱
string1 = "문자열인덱싱슬라이싱"
print(string1[0])
print(string1[-1])
print(string1[2:5])
print(string1[2:])
print(string1[:5])
print(string1)#문자열 선택 연산자로 슬라이스해도 원본은 변하지 않음
print(len(string1)) #함수가 여러 번 중첩 시 괄홀 안쪽부터 실행
print(string1.count('싱'))
print()

#print("문자열"[4]) #Index Error

string18 = """  This is Strig
"""
print(string18.upper())
print(string18.lower())

#strip() 함수
print(string18.strip())
print(string18.rstrip())
print(string18.lstrip())

#문자열의 구성 파악
string18.isalnum() #문자열이 알파벳or숫자로만 구성되었는지 확인
string18.isalpha() #문자열이 알파벳으로만 구성되었는지 확인
string18.isidentifier() #문자열이 식별자로 사용할 수 있는지 확인
string18.isdecimal() #문자열이 정수 형태인지 확인
string18.isdigit() #문자열이 숫자로 인식될수 있는지 확인
string18.isspace() #문자열이 공백으로만 구성되었는지 확인
string18.islower() #문자열이 소문자로만 구성되었는지 확인
string18.isupper() #문자열이 대문자로만 구성되었는지 확인

#in연산자
print("안녕" in "안녕하세요")
print()

#split() 함수
string19 = "1 2 3 4 5 6 7 8 9 10".split(" ")
print(string19)

string20 = "This is Strig"
for i in string20 :
    print(i.upper())
print(string20[::-1]) #확장 슬라이싱
print()

#join() 함수
list1 = ["12", "13", "14"]
print(':'.join(list1)) #:를 separate로 사용
print()



#raw string
print(r"raw string\n")
print()

var2 = "2+3"
i = 3
print(eval(var2)) #문자열로 표시된 수식 계산
#eval('i = i+5') #syntax error
exec('i = i+5')
print(i)
print()

var3 = "This is Strig"
print(var3.capitalize())
print(var3.title())




