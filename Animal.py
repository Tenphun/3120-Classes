class Animal:
    def __init__(self, name, species, gender):
        self.__name = name
        self.__species = species
        self.__gender = gender
        print("hello I am", self.__name)



    def walk(self, walk):
        self.__walk = walk
        print("I hate to", self.__walk)
    
    def lift(self,lift):
        self.__lift = lift
        print("I can lift more than", self.__lift)

    def talk(self):
        print(self.__name)

    def print_species(self):
        print("I am a",self.__species)

    def print_gender(self):
        print("I am a",self.__gender)

    def excrete_waste(self):
        print("I have excreted my waste")

    

