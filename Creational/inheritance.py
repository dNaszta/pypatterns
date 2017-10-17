class Pet(object):
    """Base class for all pets"""
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)


class Dog(Pet):
    def __init__(self, name, chases_cats):
        super().__init__(name, "Dog")
        self.chases_cats = chases_cats

    def get_chases_cats(self):
        return self.chases_cats

    def __str__(self):
        additional_info = ""
        if self.chases_cats:
            additional_info = " who chases cats"
        return super().__str__() + additional_info


p = Pet('Polly', 'parrot')
print(p)
d = Dog('Fred', True)
print(d)
print(Dog.__bases__)
print(Pet.__subclasses__())
