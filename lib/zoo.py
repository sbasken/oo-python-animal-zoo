from lib.animal import Animal

class Zoo:

    all = []
    
    def __init__(self, name, location):
        self.name = name
        self.location = location
        Zoo.all.append(self)
        
        self.species = []

    @property
    def animals(self):
        return [ animal for animal in Animal.all if animal.zoo == self.name]
    
    def animal_species(self):
        for animal in Animal.all:
            if (animal.zoo == self.name) and (animal.species not in self.species):
                self.species.append(animal.species)
        return self.species
    
    def find_by_species(self, species):
        return [ animal for animal in self.animals if animal.species == species]
    
    def animal_nicknames(self):
        return [ animal.nickname for animal in self.animals if animal.zoo == self.name]

lincoln = Zoo("lincoln", "chicago")
woodland_park = Zoo("woodland park", "seattle")
print(Zoo.all)