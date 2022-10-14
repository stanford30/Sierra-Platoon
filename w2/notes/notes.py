# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * self.length + 2 * self.width


# # Here we declare that the Square class inherits from the Rectangle class
# class Square(Rectangle):
#     def __init__(self, length):
#         super().__init__(length, length)


# square = Square(4)
# print(square.perimeter())
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f"{self.name} eats a {food}.")

    def speak(self):
        print("I'm an animal!")


class Dog(Animal):
    def __init__(self, name, is_service_animal):
        # use the logic from the parent Animal class without duplicating code
        # parent_instance = super()
        # parent_instance.__init__(name)
        super().__init__(name)

        # add some Dog-specific setup
        self.is_service_animal = is_service_animal

    def speak(self):
        print("BARK BARK!")


class Cat(Animal):
    def speak(self):
        print("meow meow!")


sparky = Dog("sparky", True)
print(sparky.name)
