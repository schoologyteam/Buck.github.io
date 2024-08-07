import random
from game.items import *

class Dealer:
    def __init__(self):
        self.lives = 0
        self.dealer_items = []
        self.last_bullet = None
        self.handcuffed = False
    
    def assign_life_to_dealer(self, round):
        if round == 1:
            self.lives = 2
        elif round == 2:
            self.lives = 4
        elif round == 3:
            self.lives = 6
    
    def assign_items_to_dealer(self,round):
        if len(self.dealer_items) == 8:
            return
        num_items = 0
        if round == 2:
            num_items = 2
        elif round == 3:
            num_items = 4
        
        additional_items_needed = min(num_items, 8 - len(self.dealer_items))
        new_items = random.choices(ITEMS, k=additional_items_needed)
        
        self.dealer_items.extend(new_items)
    
    def clear_items(self):
        self.dealer_items = []
    
    def remove_item(self, item_name):
        self.dealer_items.remove(item_name)
        
    def dealer_has_life(self):
        return self.lives > 0
    
    def show_lives(self):
        print(f"Dealer has {self.lives} lives left.")
    
    def last_known_bullet(self):
        return self.last_bullet

    def show_all_items(self):
        print(f"Dealer has the following items: {self.dealer_items}")
    
    def is_item_present(self, item):
        if item in self.dealer_items:
            return True
        else:
            return False