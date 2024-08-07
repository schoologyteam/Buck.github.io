from game.player import Player
from game.dealer import Dealer
from game.gun import Shotgun

def give_player_choice(gun: Shotgun, player: Player, dealer: Dealer):
    while True:
        print("Who do you want to shoot.\nType 1: For yourself\nType 2: For dealer\n")
        choice = input("")
        if choice == "1":
            return gun.shoot(player,dealer)
        if choice == "2":
            return gun.shoot(dealer,player)
        else:
            print("Invalid choice. Please try again.")

def game_round(gun: Shotgun, player: Player, dealer: Dealer, round: int):
    player_turn = True
    while player.player_has_lives() or dealer.dealer_has_life():
        if player_turn:
            print(f"Round {round}. {player.name}'s turn.")
            result = give_player_choice(gun,player,dealer)
            if result:
                player_turn = False
        else:
            print(f"Round {round}. Dealer's turn.")
            result
            if result:
                player_turn = True
        print(f"{player.name} lives: {player.lives}, Dealer lives: {dealer.lives}")