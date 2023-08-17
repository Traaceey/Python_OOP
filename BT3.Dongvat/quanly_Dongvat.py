class Animal:
    def __init__(self,name, species, age):
        self.name=name
        self.species=species
        self.age=age
    
    def animal_sound(self):
        if self.species == "Dog":
            print("Woof!")
        elif self.species == "Cat":
            print("Meow!")
        else:
            print("I don't know what sound this animal makes.")

    def display_infor(self):
        print("Name:",self.name)
        print("Species:",self.species)
        print("Age:",self.age)

animal1=Animal("Lucky","Dog",3)
animal1.display_infor()
animal1.animal_sound()
