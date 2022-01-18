#format() 함수
string2 = "{} {} {}".format(1, "문자열", True)
#중괄호의 개수와 format함수 괄호 안 매개변수의 개수는 반드시 같아야 함
print(string2)
print(type(string2))
print()

#정수
string3 = "{:d}".format(52)
string4 = "{:5d}".format(52)
print(string3)
print(string4)
#빈칸 0으로 채우기
string5 = "{:05d}".format(52) 
string6 = "{:05d}".format(-52)
print(string5)
print(string6)
#부호 붙이기
string7 = "{:+d}".format(52)
string8 = "{:+d}".format(-52)
print(string7)
print(string8)
#양수 부호 공백
string13 = "{: d}".format(52)
string14 = "{: d}".format(-52)
print(string13)
print(string14)
print()
#부호 뒤로 밀기
string9 = "{:+5d}".format(52)
string10 = "{:+5d}".format(-52)
print(string9)
print(string10)
#부호 앞으로 밀기
string11 = "{:=+5d}".format(52)
string12 = "{:=+5d}".format(-52)
print(string11)
print(string12)

#실수
string15 = "{:f}".format(52.273)
print(string15)
#소수점 자릿수 지정
string16 = "{:.2f}".format(52.273)
print(string16)
#의미 없는 소수점 제거
string17 = "{:g}".format(52.273)
print(string17)
print()

print("{0:^5}{1:<20}{2:>3}".format("순서", "이름", "연도"))
print("{0:^5}{1:<20}{2:>3}".format("1", "빙과", "2012"))
print()