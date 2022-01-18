t = type("타입 확인")
print(t)
print()

pi = 3.14
string = "문자열"
string += "!"
string *= 3
print(string)
print()

var1 = input("입력하세요> ")
print(var1)
print(type(var1)) #모두 문자열로 받음
print()

#스왑
var2 = 1
var3 = 2
print(var2, var3)
temp = var2
var2 = var3
var3 = temp
print(var2, var3)
