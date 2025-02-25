class Animal:
    def __init__(self, name):
        self.__name = name 
        print("hello, I am", self.__name)

    def talk(self):
        print("hi")

    def eat(self):
        print(self.__name, "is eating.")

    def sleep(self):
        print(self.__name, "is sleeping.")

    def cry(self):
        print(self.__name, "is crying.")

    def running(self):
        print(self.__name, "is running")