class budget:
    "Monthly budget"
    def __init__(self):
        self.food = 500
        self.ent = 100
        self.clot = 400
    def depositfood(self,amount):
        self.food = self.food+amount
    def depositcloth(self,amount):
        self.clot = self.clot+amount
    def depositente(self,amount):
        self.ent = self.ent+amount
    def withdrawente(self,amount):
        if self.ent>amount:
            self.ent = self.ent-amount
    def withdrawcloth(self,amount):
        if self.clot>amount:
            self.clot = self.clot-amount
    def withdrawfood(self,amount):
        if self.food>amount:
            self.food = self.food-amount
    

m1=budget()

print(m1.food)
m1.depositfood(100)
print(m1.food)
print(m1.clot)
m1.withdrawcloth(5)
print(m1.clot)
