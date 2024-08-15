
class Animal:
    def __init__(self, name, age):
        self.animal_name = name
        self.animal_age = age
        self.animal_noise = ""
             
    def name(self):
        print(f"Name: {self.animal_name}")

    def age(self):
        print(f"Age: {self.animal_age}")

    def animal_sound(self):
        print(f"{self.animal_name} roar is: {self.animal_noise}")



class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age, )
        self.mammal_fur = fur_color
        self.animal_noise = "Graah"
       

    def fur_color(self):
        print(f"Fur color: {self.mammal_fur}")

    

class Lion(Mammal):
    def __init__(self, name, age, fur_color, pride):
        super().__init__(name, age,fur_color)
        self.animal_pride = pride
        self.animal_noise = "Roar"
        
    def pride_name(self):
        print(f"Pride Name: {self.animal_pride}")


class LionCub(Lion):
    def __init__(self, name, age, fur_color, pride, mother):
        super().__init__(name, age, fur_color, pride)
        self.mother_ = mother
        self.animal_noise = "Meow"
    
    def mother_name(self):
        print(f"Mother: {self.mother_}")




animal = LionCub("Nala","1","Light Golden", "Pride Rock", "Sarabi")

animal.age()
animal.mother_name()





