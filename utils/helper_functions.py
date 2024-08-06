from game.player import Player
from game.dealer import Dealer
from game.gun import Shotgun

def give_player_choice(gun: Shotgun, player: Player, dealer: Dealer):
    while True:
        print("Who do you want to shoot.\nType 1: For yourself\nType 2: For dealer\n")
        choice = input("")
        if choice == "1":
            gun.shoot(player)
            break
        if choice == "2":
            gun.shoot(dealer)
            break
        else:
            print("Invalid choice. Please try again.")

def round_1(gun: Shotgun, player: Player, dealer: Dealer):
    pass