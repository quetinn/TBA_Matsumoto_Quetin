#Description Item class

class Item:

    #Constructor
    def __init__(self,name,description,weight):
        self.name = name
        self.description = description
        self.weight = weight

    #Methods
    def __str__(self):
        return  f"{self.name} : {self.description} ({self.weight} kg)"
