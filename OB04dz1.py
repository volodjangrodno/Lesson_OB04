# Задание: Применение Принципа Открытости/Закрытости (Open/Closed Principle) в Разработке Простой Игры
#
# Цель: Цель этого домашнего задание
# - закрепить понимание и навыки применения принципа открытости/закрытости (Open/Closed Principle),
# одного из пяти SOLID принципов объектно-ориентированного программирования.
# Принцип гласит, что программные сущности (классы, модули, функции и т.д.) должны быть открыты для расширения,
# но закрыты для модификации.
# Задача: Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами.
# Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия,
# не изменяя существующий код бойцов или механизм боя.
#
# Исходные данные:
# - Есть класс `Fighter`, представляющий бойца.
# - Есть класс `Monster`, представляющий монстра.
# - Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.
#
# Шаг 1:Создайте абстрактный класс для оружия
# - Создайте абстрактный класс `Weapon`, который будет содержать абстрактный метод `attack()`.
#
# Шаг 2: Реализуйте конкретные типы оружия
# - Создайте несколько классов, унаследованных от `Weapon`, например, `Sword` и `Bow`.
# Каждый из этих классов реализует метод `attack()` своим уникальным способом.
#
# Шаг 3: Модифицируйте класс `Fighter`
# - Добавьте в класс `Fighter` поле, которое будет хранить объект класса `Weapon`.
# - Добавьте метод `changeWeapon()`, который позволяет изменить оружие бойца.
#
# Шаг 4: Реализация боя
# - Реализуйте простой механизм для демонстрации боя между бойцом и монстром, исходя из выбранного оружия.
#
# Требования к заданию:
# - Код должен быть написан на Python
# - Программа должна демонстрировать применение принципа открытости/закрытости:
# новые типы оружия можно легко добавлять, не изменяя существующие классы бойцов и механизм боя.
# - Программа должна выводить результат боя в консоль.
#
# Пример результата:
# Боец выбирает меч.
# Боец наносит удар мечом.
# Монстр побежден!
# Боец выбирает лук.
# Боец наносит удар из лука.
# Монстр побежден!

### Шаг 1: Создание абстрактного класса для оружия


from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self, monster):
        pass



### Шаг 2: Реализация конкретных типов оружия


class Sword(Weapon):
    def __init__(self, weapon_type, name):
        self.weapon_type = weapon_type
        self.name = name
    def attack(self, monster):
        monster.take_damage(weapon_type='sword')



class Bow(Weapon):
    def __init__(self, weapon_type, name):
        self.weapon_type = weapon_type
        self.name = name
    def attack(self, monster):
        monster.take_damage(weapon_type='bow')




### Шаг 3: Модификация класса Fighter


class Fighter:
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon


    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon
        if self.weapon == 'sword':
            print(f"{fighter.name} разит мечом.")
        elif self.weapon == 'bow':
            print(f"{fighter.name} стреляет из лука.")
        print(f"{fighter.name} выбирает {weapon.name}.")

    def fight(self, monster):
        print(self.weapon.attack(monster))


### Шаг 4: Реализация механизма боя


class Monster:
    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.life_percentage = 100
        # Счётчики для подсчёта ударов
        self.damage_counts = {'sword': 0, 'bow': 0}

    def take_damage(self, weapon_type):


        if weapon_type == 'sword':
            action = "удар мечом"
            self.damage_counts['sword'] += 1
            if self.damage_counts['sword'] <= 3:
                self.life_percentage -= 33.33

        elif weapon_type == 'bow':
            action = "выстрел из лука"
            self.damage_counts['bow'] += 1
            if self.damage_counts['bow'] <= 2:
                self.life_percentage -= 50

        print(f"{fighter.name} наносит {action}")

        self.life_percentage = max(0, round(self.life_percentage, 0))

        print(f"Остаток жизни монстра: {self.life_percentage}%")

        # Выводим количество ударов мечом и выстрелов из лука

        print(f"Ударов мечом: {self.damage_counts['sword']}; Выстрелов из лука: {self.damage_counts['bow']}")

        if self.life_percentage <= 0:

            print("Монстр побежден!")


    def reset(self):

        self.damage_counts = {'sword': 0, 'bow': 0}
        self.life_percentage = 100
        print("Результаты схватки обнулены, монстр готов к новому бою!")




# Создаем бойца и монстра
monster = Monster("Змей Горыныч", 100)
fighter = Fighter("Илья Муромец", Sword("меч", "Меч-Кладинец"))

# Обнуляем счетчики
monster.reset()


# Выбираем оружие
weapon1 = Sword("меч", "Меч-Кладинец")
weapon2 = Bow("лук", "Лук-Самострел")

# Играем
fighter.fight(monster)

# Меняем оружие
fighter.changeWeapon(weapon2)
fighter.fight(monster)

# Добиваем монстра
fighter.changeWeapon(weapon1)
fighter.fight(monster)

