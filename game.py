from menu import main_menu
from player import Player
from map import Map
import ux

def main():

    main_menu()
    ux.cls()
    game_map = Map('maps/forge.map', 'maps/forge.objects') 
    player = Player("Nigel")

    print("~" * 20)
    player.display_stats()
    print("~" * 20)
    
    ux.system("Welcome Nigel! You are in the Queen's Forge. You must find the Queen's Crown and return it to her.\n")
    
    game_map.display_map()
    while True:
        move = input("\n: ").strip().upper()
        if move == 'QUIT':
            print("Goodbye!")
            break
        elif move == 'HELP':
            ux.cls()
            ux.system("Use N, S, E, W to move, LOOK, SAVE, or QUIT to exit.\nYou may also use GET to pick up items.")
            game_map.display_map()
        elif move in ['N', 'S', 'E', 'W']:
            ux.cls()
            success, message = game_map.move_player(move)
            ux.system(message)
            game_map.display_map()
        else:
            ux.cls()
            ux.system("Invalid input. Use N, S, E, W to move or QUIT to exit.")
            game_map.display_map()

if __name__ == '__main__':
    main()
