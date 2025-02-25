class Animal:
    def __init__(self, name):
        self.__name = name 
        print("hello, I am", self.__name)

    def talk(self, talk):
        self.__talk=talk
        print("My greeting is", self.__talk)
    
    def walk(self, walk):
        self.__walk = walk
        print("I hate to", self.__walk)
    
    def lift(self,lift):
        self.__lift = lift
        print("I can lift more than", self.__lift)


