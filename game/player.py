from game.items import *
import random
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.lives = 0
        self.player_items = []
        self.starting_money = 100000
    
    def assign_life_to_player(self, round):
        if round == 1:
            self.lives = 2
        elif round == 2:
            self.lives = 4
        elif round == 3:
            self.lives = 6
    
    def assign_items_to_player(self, round):
        if len(self.player_items) == 8:
            return
        num_items = 0
        if round == 2:
            num_items = 2
        elif round == 3:
            num_items = 4
        
        additional_items_needed = min(num_items, 8 - len(self.player_items))
        new_items = random.choices(ITEMS, k=additional_items_needed)
        
        self.player_items.extend(new_items)
    
    def clear_items(self):
        self.player_items = []
    
    def show_lives(self):
        print(f"{self.name} has {self.lives} lives left.")
    