# Pour les classes en python on doit faire obligatoirement un constructeur

class Personne:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def sepresenter(self):
        print(self.firstname)
        print(self.lastname)


class Player(Personne):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        
        # on peut appeler le construct de la classe mere de 2 façons : 
        # Personne.__init__(firstname, lastname)
        super().__init__(firstname, lastname) # l'attribut super permet d'avoir moins de code pour récuperer les héritages


p1 = Player("Luis", "Suarez")

p1.sepresenter()


# Reference
# permet de ne pas créer une copie en mémoire de la meme vairable/class etc...
A1 = Auteur("pierre", "paul")
L1 = Livre("bible", A1)