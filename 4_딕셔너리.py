dic1 = {
      "키" : 10,
      #키 : 10, #Name Error
      str : "문자열", #str은 기본 식별자가 있어서 Error를 발생시키지 않음
      1 : 20,
      False : 30,
      "스파이더맨" : ["토비 맥과이어", "앤드류 가필드", "톰 홀랜드"]
}
print(dic1)
print(dic1["키"])
print(dic1[1])
print(dic1[False])
print(dic1["스파이더맨"][0])
print()

#값 변경
dic1["키"] = 40
print(dic1["키"])
#값 추가
dic1["키2"] = 50
#값 제거
del dic1[1]
print(dic1)
print()

#in 연산자
k = input("키를 입력하세요> ")
if(k in dic1) :
  print(dic1[k])
  print(dic1.get(k))
else :
  print("키가 없습니다")
  print(dic1.get(k))
print()

#for반복문
for i in dic1 :
  print(i, dic1[i])
print()

#items함수
print(dic1.items())
for key, value in dic1.items() :
  print(key, value)
print()





