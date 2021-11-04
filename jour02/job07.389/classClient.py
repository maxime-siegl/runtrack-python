from classPersonne import Personne


class Client(Personne):
    def __init__(self, nom, prenom, collection):
        self.nom = nom
        self.prenom = prenom
        super().__init__(nom, prenom)
        self.collection = collection

    def inventaire(self):
        print(self.collection)