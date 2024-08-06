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
    while True:
        if round == 1:
            player.assign_life_to_player(round)
            dealer.assign_life_to_dealer(round)
            player.assign_items_to_player(round)
            dealer.assign_items_to_dealer(round)
            gun.load_bullets(round)
            game_round(player,dealer,round)
            dealer.show_lives()
            player.show_lives()
            round += 1
        elif round == 2:
            round += 1
            pass
        elif round == 3:
            round += 1
            pass
        else:
            print("Do you want to Continue for\n1. Double or nothing.\n2. Quit.\n")
            player_choice = input("")
            if player_choice == "1":
                round = 1
                continue
            elif player_choice == "2":
                break
        




if __name__ == "__main__":
    main()