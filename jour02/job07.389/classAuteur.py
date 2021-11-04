from classPersonne import Personne
from classLivre import Livre


class Auteur(Personne):
    def __init__(self, nom, prenom, oeuvre):
        self.nom = nom
        self.prenom = prenom
        super().__init__(nom, prenom)
        self.oeuvre = oeuvre

    def listerOeuvre(self):
        print(self.oeuvre)

    def ecrireUnLivre(self, titreAEcrire):
        newLivre = Livre(titreAEcrire)
        self.oeuvre.append(newLivre.getTitre())