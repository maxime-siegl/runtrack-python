class Livre:
    def __init__(self, titre, auteur):
        self.title = titre
        self.auteur = auteur

    def print(self):
        print(self.title)

    def getTitre(self):
        return self.title