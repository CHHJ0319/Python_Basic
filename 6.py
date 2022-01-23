#숫자로 변환되는 것만 리스트에 넣기
list1 = ["10", "52", "문자열", "7"]
list2 = []

for item in list1:
    try:
        float(item)
        list2.append(item)
    except:
        pass

print(list2)
print()

#finally구문
try:
    file1 = open("1.txt", "w")
    예외.발생()
except Exception as e:
    print(e)
#finally:
#    file1.close()

file1.close()
print(file1.closed)
print()

#try구문 내에 return
def func1():
    print("함수1 시작")
    try:
        print("try구문")
        return
        print("return 뒤")
    except:
        print("except구문")
    else:
        print("else구문")
    finally:
        print("finally구문")
    print("함수1 마지막줄")

func1()
print()

#반복문과 finally구문
while True:
    try:
        print("try구문")
        break
        print("break 뒤")
    except:
        print("except구문")
    else:
        print("else구문")
    finally:
        print("finally구문")
    print("while반복문 마지막줄")

print()

#모든 예외 처리
list3 = [1, 25, 864]
try:
    number_input = int(input("정수 입력 >"))
    print("{}번째 요소 {}".format(number_input, list3[number_input]))
    예외.발생()
except ValueError as exception:
    print("정수를 입력하시오")
    print(type(exception), exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났습니다")
    print(type(exception), exception)
except Exception as exception:
    print("예상치 못한 예외 발생")
    print(type(exception), exception)