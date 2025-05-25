from project.child import Child
from project.person import Person

if __name__ == '__main__':
    person_instance = Person(name='Peter', age=25)
    child_instance = Child(name='Peter Junior', age=5)
    print(person_instance.name)
    print(person_instance.age)
    print(child_instance.__class__.__bases__[0].__name__)
