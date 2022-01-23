#부모 클래스
class Parent:
    def __init__(self):
        self.name = "부모 클래스"
        print("부모 클래스 __init__()")

    def method(self):
        print("부모 클래스의 메소드") 

#자식 클래스
class Child:
    def __init__(self):
        self.name = "자식 클래스"
        print("자식 클래스 __init__()")

    def method(self):
        print("자식 클래스의 메소드") 

#예외 클래스
class CustomException(Exception):
    def __init__(self):
        Exception.__init__(self)
        print("내가 만든 오류")

    #오버라이드 
    def __str__(self):
        return "오류 발생"

    #새로운 함수 정의
    def print(self):
        print("새로운 함수")

child = Child()
child.method()
print(child.name)
print()

#Exception 클래스를 상속했으므로 raise로 예외 발생시키는 것 가능
try:
    raise CustomException
except CustomException as e:
    e.print()
