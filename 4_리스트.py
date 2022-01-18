list1 = ["요소1", "요소2", 1, 2, True, False, ["요소3", 4]]
print(list1[0:3])
print(list1[-2])  
#이중으로 사용 가능
print(list1[0][0]) 
print(list1[6][0])
#요소 변경
list1[3] = 3
print(list1) 
#in/not in
print("요소1" in list1)
print("요소1" not in list1)
#for반복문
for element in list1 :
    print(element)
print()

list2 = [2, 5, 6, 1, 7, 3, 9, 4, 8, 2]
print(max(list2))
print(min(list2))
print(sum(list2))
list2.sort()
print(list2)
print()

#reversed() 함수
list2_reverse = reversed(list2)
print(list2_reverse)
print(list(list2_reverse))
#for i in list3_reverse :
#    print("첫번째 {}".format(i))
#for i in list3_reverse :
#    print("두번째 {}".format(i))
#reversed() 함수 결과가 제너레이터이기 때문에 여러번 활용 안함
for i in reversed(list2) :
    print("첫번째 {}".format(i))
for i in reversed(list2) :
    print("두번째 {}".format(i))
#그래서 for구문 내부에 곧바로 넣어서 사용
print(list2[::-1]) #확장 슬라이싱
print()

#enumerate() 함수
print(enumerate(list2))
print(list(enumerate(list2)))
for i, value in enumerate(list2) :
    print(i, value)
print()

#리스트 내포
list3 = [i * i for i in range(0, 20+1, 2)]
print(list3)
list3 = [i * i for i in range(0, 20+1, 2) if i%4==0] 
print(list3)
print()



print(list2.count(2))
print(list2.index(1))
list2.reverse()
print(list2)
print()

string = "문자열 입니다"
list5 = string.split()
print(list5) 
print()





