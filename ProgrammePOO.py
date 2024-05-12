class Voiture:
    def __init__(self, marque, vitesse, prix):
        self.marque = marque
        self.vitesse = vitesse
        self.prix = prix

    def afficher_prix(self):
        print("Le prix de la voiture est de", self.prix, "euros")

    def afficher_vitesse(self):
        print("La vitesse de la voiture est de", self.vitesse, "km/h")

    def afficher_marque_et_vitesse(self):
        print(f"La voiture de marque {self.marque} a une vitesse de {self.vitesse} km/h")

mercedes = Voiture(marque="Mercedes", vitesse=200, prix=90000)

mercedes.afficher_prix()
mercedes.afficher_vitesse()
mercedes.afficher_marque_et_vitesse()

