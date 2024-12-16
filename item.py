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
