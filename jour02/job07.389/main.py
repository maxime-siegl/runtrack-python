from classAuteur import Auteur
from classClient import Client

class Bibliotheque:
    def __init__(self, nom, catalogue):
        self.nom = nom
        self.catalogue = catalogue

    def acheterLivre(self, auteur, titreLivre, quantite):
        if titreLivre in auteur.listerOeuvre():
            newEnter = {titreLivre:quantite}
            self.catalogue.update(newEnter)

    def inventaire(self):
        print(self.catalogue)

    def louer(self, client, nomLivre):
        if nomLivre in self.catalogue and self.catalogue[nomLivre] > 0:
            client.catalogue.append(nomLivre)
            quantiteActuelle = self.catalogue[nomLivre] - 1
            self.catalogue[nomLivre].update(quantiteActuelle)

    def rendreLivres(self, client):
        nombreLivre = len(client.catalogue)
        i = 0
        while i < nombreLivre:
            #actualiser ou ajouter ?
            print(client.catalogue[i])
            i += 1


biblio = Bibliotheque("BiblioTek", {"Batman vs Joker":2, "Romeo et Juliette":15})
biblio.inventaire()