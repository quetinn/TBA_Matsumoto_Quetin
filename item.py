#Description Item class

class Item:

    # Constructeur
    def __init__(self,name,description,weight):
        self.name = name
        self.description = description
        self.weight = weight

    # Representation string
    def __str__(self):
        return  f"{self.name} : {self.description} ({self.weight} kg)"
    
    # Representation string pour les container type set ou list
    def __repr__(self):
        return self.__str__()
    
    # Redéfinir __eq__ pour comparer les objets par leurs attributs
    def __eq__(self, other):
        if isinstance(other, Item):
            return (
                self.name == other.name and
                self.description == other.description and
                self.weight == other.weight
            )
        return False

    # Redéfinir __hash__ pour permettre l'utilisation dans des sets
    def __hash__(self):
        return hash((self.name, self.description, self.weight))
