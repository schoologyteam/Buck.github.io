class Dealer:
    def __init__(self):
        self.lives = 0
        self.items = []
    
    def assign_life_to_dealer(self, round):
        if round == 1:
            self.lives = 2
        elif round == 2:
            self.lives = 4
        elif round == 3:
            self.lives = 6
    
    def assign_items_to_dealer(self):
        pass