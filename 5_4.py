#파일 처리
file1 = open("1.txt", "w")
file1.write("첫번째 파일 처리 문서입니다.")
file1.close()

with open("1.txt", "r") as file2 :
    contents = file2.read()

print(contents)
print(file2.closed) #파일을 제대로 닫았는지 확인
print()

with open("2.txt", "w") as file3 :
    file3.writelines(["줄바꿈이",\
        "가능한가",\
        "띄어쓰기는",\
        "가능한가"])
    #file3.writelines([True, 273, "문자열"]) #문자열 리스트만 가능


#제너레이터
def func1():
    print("함수가 호출되었습니다.")
    yield "func1"

func1()
print(func1()) #제너레이터 객체

def func2():
    print("A 지점 통과")
    yield "1"
    print("B 지점 통과")
    yield "2"
    print("C 지점 통과")

output = func2()
a = next(output)
print(a)
print("D 지점 통과")
b = next(output)
print(b)
c = next(output)
print(c)
next(output)