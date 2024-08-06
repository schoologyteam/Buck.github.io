from game.player import Player
from game.dealer import Dealer
from game.gun import Shotgun
from utils.helper_functions import *

def main():
    name = input("")
    player = Player(name)
    dealer = Dealer()
    round = 1
    gun = Shotgun()
    
    print("\n" + "="*20)
    player.assign_life_to_player(round)
    dealer.assign_life_to_dealer(round)
    player.assign_items_to_player(round)
    dealer.assign_items_to_dealer(round)
    gun.load_bullets(round)
    give_player_choice(gun,player,dealer)
    dealer.show_lives()
    player.show_lives()
    




if __name__ == "__main__":
    main()