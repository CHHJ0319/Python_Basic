#팩토리얼
def factorial(n):
    if n == 0:
        return 1
   
    return n * factorial(n-1) #조기 리턴

print(factorial(5))
print()

#피보나치 수열
dict1 = {
    1: 1,
    2: 2
}

def fibonacci(n):
    if n in dict1:
        return dict1[n]
    #조기 리턴
    output = fibonacci(n-1) + fibonacci(n-2)
    dict1[n] = output
    return output

print(fibonacci(50))
print()

#리스트 평탄화
def flatten(data):
    output = []
    for item in data:
        if type(item) == list :
            output += flatten(item)
        else:
            output.append(item)
    return output

list1 = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print(flatten(list1))
