class SampleClass:


    def __init__(self):
        self.__a = 10
        print(self.__a)


    def get_a(self):
        print("set",self.__a)


    def set_a(self):
        self.__a = 20
        print("set",self.__a)



b1 = SampleClass()
b1.set_a()
b1.get_a()
