from project.animals.animal import Mammal
from project.food import Food, Vegetable, Fruit, Meat, Seed


class Mouse(Mammal):
    def make_sound(self) -> str:
        return 'Squeak'

    def feed(self, food: Food) -> str:
        if not isinstance(food, (Vegetable, Fruit)):
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += 0.10 * food.quantity
        self.food_eaten += food.quantity

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]'


class Dog(Mammal):
    def make_sound(self) -> str:
        return 'Woof!'

    def feed(self, food: Food) -> str:
        if not isinstance(food, Meat):
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += 0.40 * food.quantity
        self.food_eaten += food.quantity

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]'


class Cat(Mammal):
    def make_sound(self) -> str:
        return 'Meow'

    def feed(self, food: Food) -> str:
        if not isinstance(food, (Vegetable, Meat)):
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += 0.30 * food.quantity
        self.food_eaten += food.quantity


class Tiger(Mammal):
    def make_sound(self) -> str:
        return 'ROAR!!!'

    def feed(self, food: Food) -> str:
        if not isinstance(food, Meat):
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += 1.00 * food.quantity
        self.food_eaten += food.quantity
