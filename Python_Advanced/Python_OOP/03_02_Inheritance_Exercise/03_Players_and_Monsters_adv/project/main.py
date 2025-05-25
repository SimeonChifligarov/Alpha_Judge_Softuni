from project.elf import Elf
from project.hero import Hero

if __name__ == '__main__':
    hero_instance = Hero(username='H', level=4)
    print(hero_instance.username)
    print(hero_instance.level)
    print(str(hero_instance))
    elf_instance = Elf(username='E', level=4)
    print(str(elf_instance))
    print(elf_instance.__class__.__bases__[0].__name__)
    print(elf_instance.username)
    print(elf_instance.level)
