class Bank_account:
    def __init__(self, idNumber, nameUser, solde):
        self.idNumber = idNumber
        self.nameUser = nameUser
        self.solde = solde

    def versement(self, argent):
        self.solde = self.solde + argent

    def retrait(self, argent):
        if(self.solde < argent):
            print("Impossible d'effectuer cette action. Solde insuffisant")
        else:
            self.solde = self.solde - argent

    def agios(self):
        self.solde = self.solde * 95/100

    def showMonnaie(self):
        print("Numéro de compte:" + self.idNumber)
        print("Nom & prémon du proprio de la carte" + self.nameUser)
        print("Solde" + self.solde)
        print("Sauf erreur ou omission")

# TEST de la classe
dede = Bank_account(5436798, "John Doe", 1500)