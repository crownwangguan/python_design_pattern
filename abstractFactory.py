class Dog:

    """A simple dog class"""

    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"


class Cat:

    """A simple cat class"""

    def speak(self):
        return "Meow!"

    def __str__(self):
        return "Cat"


class DogFactory:
    """Concrete Factory"""
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "Dog Food!"


class CatFactory:
    """Concrete Factory"""
    def get_pet(self):
        return Cat()

    def get_food(self):
        return "Cat Food!"


class PetStore:
    """PetStore houses our Abstract Facotry"""
    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory

    def show_pet(self):
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print "Our pet is '{}'".format(pet)
        print "Our pet says hello by '{}'".format(pet.speak())
        print "Its food is '{}'".format(pet_food)


dogFactory = DogFactory()
catFactory = CatFactory()

dogShop = PetStore(dogFactory)
dogShop.show_pet()

catShop = PetStore(catFactory)
catShop.show_pet()

