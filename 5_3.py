tuple1 = (10, 20, 30)
tuple2 = (1,) #요소를 하나만 가지는 튜플

(a, b) = (2, 3)
print(a, b)
print()

#괄호가 없는 튜플
tuple3 = 4, 5, 6
print(type(tuple3))
x, y, z = 7, 8, 9
print(x, y, z)
print()

#변수의 값 교환
a, b = b, a
print(a, b)
print()

#divmod()함수
quo, rem = divmod(10, 4)
print(quo, rem) #몫, 나머지
print()

#함수의 매개변수로 함수 전달하기
def call_function(func):
    for i in range(3):
        func()

def print_hello():
    print("hello")

call_function(print_hello)
print()

#람다
print((lambda x, y: x + y)(10, 20))

#map(), filter() 함수
list1 = [1, 2, 3]
#power = lambda x: x * x
#under_3 = lambda x : x < 3

#output_1 = map(power, list1)
output_1 = map(lambda x: x * x, list1)
print(output_1)
print(list(output_1))

#output_2 = filter(under_3, list1)
output_2 = filter(lambda x : x < 3, list1)
print(output_2)
print(list(output_2))