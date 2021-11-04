class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom
    
    def getPrenom(self):
        return self.prenom

    def setPrenom(self, prenom):
        self.prenom = prenom

    def SePresenter(self):
        return self.nom + ' ' + self.prenom


p1 = Personne("Curry", "Stephen")
p2 = Personne("LaVine", "Zack")
p3 = Personne("Antetokounmpo", "Giannis")

print(p1.getNom(), p1.getPrenom())
p1.setNom("Thomson")
p1.setPrenom("Klay")
print(p1.getNom(), p1.getPrenom())
