# class SmartHouse():
#     def turn_on_light(self):
#         pass
#
#     def turn_on_tv(self):
#         pass
#
#     def turn_on_heater(self):
#         pass
#
#     def turn_on_ac(self):
#         pass


# принцип разделения интерфейсов (Interface Segregation Principle)

class Lights():
    def turn_on_light(self):
        print("Свет включен")

class TV():
    def turn_on_tv(self):
        print("Телевизор включен")

class Heater():
    def turn_on_heater(self):
        print("Отопитель включен")

class AC():
    def turn_on_ac(self):
        print("Кондиционер включен")