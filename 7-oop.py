# class Sample:
#     pass
#
# my_sample = Sample()
# print(my_sample)
# print(type(my_sample))


# class Dog:
#     #Static equivalent, attribute class wide, not specific to instance
#     species = 'Mammal'
#     def __init__(self, breed, name):
#         self.breed = breed
#         self.name = name
#
#     def bark(self):
#         print(f"Woof!: {self.name}")
#
#     def bark2(self, number):
#         print(f"Woof!: {self.name}, {number}")
#
# my_dog = Dog('Lab', "Dog1")
# print(my_dog.species)
# print(Dog.species)
# print(my_dog.breed)
# my_dog.bark()
# my_dog.bark2(1132)


# class Animal:
#     def __init__(self):
#         print("Animal created!")
#     def who_am_i(self):
#         print("I am Animal")
#     def eat(self):
#         print("I am Eating")
#
# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print("Dog created!")
#
#     def who_am_i(self):
#         print("I am Dog")
#
#     def bark(self):
#         print("I am Barking")
#
# mydog = Dog()
# mydog.who_am_i()
# mydog.eat()
# mydog.bark()


#
#
# class Dog:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         return self.name + " says woof!"
#
# class Cat:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         return self.name + " says meow!"
#
# niko = Dog("Niko")
# felix = Cat("Felix")
#
# print(niko.speak())
# print(felix.speak())
#
# def pet_speak(my_pet):
#     return my_pet.speak()
#
# print(pet_speak(niko))
#
#
# for pet in [niko, felix]:
#     print(type(pet))
#     print(pet.speak())
#
#
# print(pet_speak(felix))
# print(pet_speak(niko))

#
# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         raise NotImplementedError("Subclass must implement this abstract method")
#
# class Dog(Animal):
#     pass
#
# class Cat(Animal):
#     def speak(self):
#         return f"Meow!: {self.name}"
#
# fido = Dog("Fido")
# isis = Cat("Isis")
#
# print(fido.speak())
# print(isis.speak())
