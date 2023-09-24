class Market:
    def __init__(self):
        self.true_values=makeBank()
    def buy(self, x, y):
        x.bank[y]+=100
        x.bank["gold"]-=self.true_values[y]*1.3    
        self.true_values[y]+=3
    def sell(self, x, y):
        pass