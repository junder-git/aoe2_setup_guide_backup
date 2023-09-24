class Market:
    def __init__(self):
        self.true_values={"food":100, "wood":100, "stone":100}
    def buy(self, x, y):
        x.bank[y]+=100
        x.bank["gold"]-=self.true_values[y]*1.3    
        self.true_values[y]+=3
    def sell(self, x, y):
        pass