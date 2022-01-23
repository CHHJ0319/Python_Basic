class Class2():

    def __init__(self, name):
        self.__name = name #프라이빗 변수

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    #데코레이션을 사용한 게터
    @property
    def name(self):
        return self.__name

    #데코레이션을 사용한 세터
    @name.setter
    def name(self, value):
        self.__name = value
    


    

instance1 = Class2("인스터스1")

# print(Class2.__name)
print(instance1.get_name())
instance1.set_name("인스턴스2")
print(instance1.get_name())
print()

print(instance1.name)
instance1.name = "인스턴스3"
print(instance1.name)
print()