class BankAccount:
    def __init__(self, cardNumber, nameUser, soldCard):
        self.cardNumber = cardNumber
        self.nameUser = nameUser
        self.soldCard = soldCard

    def payment(self, money):
        self.soldCard = self.soldCard + money

    def showCash(self):
        print("Numéro de compte:", self.cardNumber)
        print("Proprio de la carte:", self.nameUser)
        print("Solde:", self.soldCard, "euros")

dede = BankAccount(16168891, "John Doe", 15000)
dede.payment(1000)
dede.showCash()