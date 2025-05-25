from project.lizard import Lizard
from project.mammal import Mammal

if __name__ == '__main__':
    mammal_instance = Mammal(name='Stella')
    print(mammal_instance.__class__.__bases__[0].__name__)
    print(mammal_instance.name)
    lizard_instance = Lizard(name='John')
    print(lizard_instance.__class__.__bases__[0].__name__)
    print(lizard_instance.name)
