class Animal:
    def __init__(self, name, age, color, hp = 100):
        self.__name = name 
        self.__age = age
        self.__color = color
        self.__hp = hp
        print("hello, I am", self.__name)
    
    def age(self):
        print (f'Today i turn, {self.__age} years old')
        
    def color(self):
        print (f'I can camoflauge in areas that are dark since my color is, {self.__color}')

    def battle(self):
        self.__hp -=1
        print ("ROAR")
        print (f'You have {self.__hp}, hp left in the tank (-1 hp)')

    def rest(self):
        print ("HUFF")
        print (f'You have {self.__hp}, hp left in the tank (+1 hp)')
    

