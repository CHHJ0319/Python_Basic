class Class1():
    
    class_var = "클래스 변수"

    class_list = []

    @classmethod
    def print(cls):
        print("클래스 함수 실행")
        for inst in cls.class_list:
            print(str(inst))

    def __init__(self, name):
        #print("인스턴스가 생성되었습니다.")
        self.name = name
        #print("클래스 내부에서 {} 호출".format(Class1.class_var))
        Class1.class_list.append(self)

    def __del__(self):
        #print("인스턴스가 소멸되었습니다.")
        pass

    def __str__(self):
        return self.name

    def __eq__(self, value):
        if not isinstance(value, Class1):
            raise TypeError("Class1의 인스턴스만 비교 가능")
        return self.name == value.name 

    

Class1("인스턴스")
instance1 = Class1("인스터스1")

print(isinstance(instance1, Class1)) #상속 관계 확인 O
print(type(instance1) == Class1) #상속 관계 확인 X
print()

print(str(instance1))
print()

#instance1 == 10

print("클래스 외부에서 {} 호출".format(Class1.class_var))
print()

instance2 = Class1("인스터스2")
instance3 = Class1("인스터스3")
Class1.print()
