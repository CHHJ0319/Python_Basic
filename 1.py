#개발전용폰트
D2Coding = "https://github.com/naver/d2codingfont"
나눔고딕코딩글꼴 = "https://github.com/naver/nanumfont"

print ("Hello World")
print() #줄 바꿈

#주석

#키워드 리스트
import keyword
print(keyword.kwlist) #대소문자 구분
print()

#파이썬에서 첫번째 글자가 소문자인 캐멀케이스는 안씀 ex) camelCase

#print
print(1, 2, "여러","개","출력")
print("separament", "확인", sep = '*')
print("end 확인", end = 'End\n')
print()

#진수 변환
print("{:b}".format(10)) #10진수 -> 2진수
print(int("1010", 2)) #2진수 -> 10진수
print("{:o}".format(10)) #10진수 -> 8진수
print(int("12", 8)) #8진수 -> 10진수
print("{:x}".format(10)) #10진수 -> 16진수
print(int("a", 16)) #16진수 -> 10진수
print()

#예제 1~100사이의 숫자 중 2진수로 변환했을 대 0이 하나만 포함된 수
list1 = [i for i in range(1, 100+1) if "{:b}".format(i).count("0") == 1]
for i in list1 :
    print("{} : {}".format(i, "{:b}".format(i)))