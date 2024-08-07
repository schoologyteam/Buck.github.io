from game.gun import Shotgun
from game.player import Player
from game.dealer import Dealer
import random

ITEMS = ["Beer", "Cigarette pack", "Hand saw", "Magnifying glass", "Handcuffs"]

DOUBLE_OR_NOTHING = ["Adrenaline", "Inverter", "Expired Medicine", "Burner Phone", "Beer", "Cigarette pack", "Hand saw", "Magnifying glass", "Handcuffs"]

def call_functions_by_items(item, player: Player, dealer: Dealer):
    if item == "Beer":
        return use_beer()
    elif item == "Cigarette pack":
        return use_cigarette_pack()
    elif item == "Hand saw":
        return use_hand_saw()
    elif item == "Magnifying glass":
        return use_magnifying_glass()
    elif item == "Handcuffs":
        return use_handcuffs()
    elif item == "Adrenaline":
        return use_adrenaline()
    elif item == "Inverter":
        return use_inverter()
    elif item == "Expired Medicine":
        return use_expired_medicine()
    elif item == "Burner Phone":
        return use_burner_phone()




def use_beer(gun: Shotgun, dealer: Dealer, user):
    bullet = gun.eject_bullet()
    dealer.last_bullet = bullet
    if isinstance(user, Dealer):
        user.remove_item("Beer")
    if isinstance(user, Player):
        user.remove_item("Beer")
    
def use_cigarette_pack(target):
    if isinstance(target, Dealer) or isinstance(target, Player):
        target.lives += 1
        target.remove_item("Cigarette pack")
        
def use_hand_saw(gun: Shotgun, user):
    gun.change_barrel()
    if isinstance(user, Dealer):
        user.remove_item("Hand saw")
    if isinstance(user, Player):
        user.remove_item("Hand saw")
    
    
def use_magnifying_glass(gun: Shotgun, user):
    if isinstance(user, Dealer):
        user.remove_item("Magnifying glass")
    if isinstance(user, Player):
        user.remove_item("Magnifying glass")
    return gun.current_bullet()

def use_handcuffs(user):
    if isinstance(user, Dealer):
        user.remove_item("Handcuffs")
        user.handcuffed = True
    if isinstance(user, Player):
        user.remove_item("Handcuffs")
        user.handcuffed = True
    
    
    
def use_adrenaline(user, other):
    if isinstance(user, Dealer):
        user.remove_item("Adrenaline")
        if isinstance(other, Player):
            dealer_choice = random.choice(other.player_items)
            other.remove_item(dealer_choice)
    if isinstance(user, Player):
        user.remove_item("Adrenaline")
        if isinstance(other, Dealer):
            other.show_all_items()
            while True:
                player_choice = input("What item do u want to take from the Dealer:\t")
                if other.is_item_present(player_choice):
                    other.remove_item(player_choice)
                    break
                else:
                    print("Dealer doesn't have that item")
                    continue
    
def use_inverter():
    pass
def use_expired_medicine():
    pass
def use_burner_phone():
    pass