# class Bird():
#     def __init__(self, name):
#         self.name = name
#
#     def fly(self):
#         print(f"{self.name} - эта птица летает")
#
# class Pinguin(Bird):
#     pass
#
# pinguin = Pinguin("Sara")
# pinguin.fly()


# принцип подстановки Барбары Лисков (Liskov substitution Principle)

class Bird():
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} - эта птица летает")

class Duck(Bird):
    def __init__(self, name):
        super().__init__(name)
    def fly(self):
        print(f"{self.name} - эта птица не только летает, но и плавает")

def fly_in_the_sky(animal):
    animal.fly()

b = Bird("Синичка")
d = Duck("Кряква")

fly_in_the_sky(b)
fly_in_the_sky(d)
