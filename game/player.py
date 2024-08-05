class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.lives = 0
        self.items = []
        self.starting_money = 100000
    
    def assign_life_to_player(self, round):
        if round == 1:
            self.lives = 2
        elif round == 2:
            self.lives = 4
        elif round == 3:
            self.lives = 6
    
    def assign_items_to_player(self):
        pass
    
        