#예제1
list1 = [1, 11, 111, 1111, 11111]
for i in list1 :
    print("{}의 자릿수는 {}".format(i, len(str(i))))
print()

#예제2
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]
for i in list2 :
    output[(i+2)%3].append(i)
print(output)
print()

#예제3
list3 = [
  {"제목" : "스파이더맨", "연도" : 2002},
  {"제목" : "어메이징 스파이더맨", "연도" : 2012},
  {"제목" : "스파이더맨: 홈커밍", "연도" : 2017}
]
for element in list3:
  print(element["제목"], str(element["연도"])+"년")
print()

#예제4
list4 = [1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3,5, 4, 8, 9, 7, 2, 3]
dict1 = {}
for element in list4 :
  if element not in dict1 :
    dict1[element] = 1
  else :
     dict1[element] += 1
print(dict1)
print()

#예제5
dict2 = {
  "name" : "그리드맨",
  "union" : {
    "강력" : "맥스 그리드맨",
    "무장" : "버스터 그리드맨",
    "대공" : "스카이 그리드맨"
  },
  "final" : ["초합체초인", "풀파워 그리드맨"]
}
for key in dict2 :
  if type(dict2[key]) is str :
    print(dict2[key])
  elif type(dict2[key]) is dict :
    for i in dict2[key] :
      print(i + "합체초인 " + dict2[key][i])
  elif type(dict2[key] is list) :
    for j in dict2[key] :
      print(j)
print()

#예제6
list5 = ["직업", "레벨"]
list6 = ["기사", 3]
dict3 = {}
for i in range(0, len(list5)) :
    dict3[list5[i]] = list6[i]
print(dict3)

#예제7
max_val = 0
a = 0
b = 0
for i in range(1,(100//2+1)) :
    j = 100-i
    val = i*j
    if val > max_val:
        a = i
        b = j
        max_val = val

print(a, b, max_val)