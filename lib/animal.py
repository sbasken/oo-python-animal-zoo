# import ipdb

class Animal:
    all = []

    def __init__(self, species, numerical, nickname, zoo):
        self.species = species
        self.numerical = numerical
        self.nickname = nickname
        self.zoo = zoo
        self.weight = 0
        Animal.all.append(self)

    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @classmethod
    def find_by_species(cls, species):
        return [animal for animal in Animal.all if animal.species == species]

koko = Animal("dog", 3, "kochan", "woodland park")
clause = Animal("dog", 6, "clause", "woodland park")
rose = Animal("cat", 3, "rose", "lincoln")
peach = Animal("cat", 5, "peach", "lincoln")
cookie = Animal("elephant", 10, "cookie", "lincoln")

