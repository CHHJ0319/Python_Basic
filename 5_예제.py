#예제1 사람들을 여러 개의 테이블에 나누는 패턴
min_people = 2 #테이블 당 최소 사람 수
max_people = 10 #테이블 당 최대 사람 수
total_people = 100
memo = {}

def sit_table(rest, sit):
    key= str([rest, sit])
    if key in memo:
        return memo[key]
    if rest < 0:
        return 0
    if rest == 0:
        return 1
    
    count = 0 #패턴
    for i in range(sit, max_people+1):
        count += sit_table(rest-i, i)
    memo[key] = count
    return count

print(sit_table(total_people, min_people))
print()

#예제2
numbers1 = [1, 2, 3]
print("::".join(map(str,numbers1)))
print()

#예제3
numbers2 = list(range(1, 10+1))
print("홀수")
print(list(filter(lambda x : x%2 == 1, numbers2)))
print("3 이상 7 미만")
print(list(filter(lambda x : 3<= x <7, numbers2)))
print("제곱해서 50 미만")
print(list(filter(lambda x : x*x <50, numbers2)))


