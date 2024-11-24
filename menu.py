import ux

def main_menu():

    choice = None
    while choice != '1':
        ux.cls()
        print(f"Oi, 'ello there, oym Nigel! Welcome ter the {ux.EM}Queen's Forge{ux.RST}, it is! You ready ter crack on, then?\n")
        print("1. Oy, what's all this then?\n")
        choice = input("\nEnter your choice: ")

    name = ''
    while name.upper() != 'NIGEL':
        ux.cls()
        print("Right, then! Let's get ter it, shall we? What's yer name, then?\n")
        ux.system("Your name is also 'Nigel'")
        name = input("\nEnter your name: ")

    ux.cls()
    print(f"Right, then, {name}! Swing by the {ux.EM}forge{ux.RST}, mate, an' we'll get crackin' on sharpish-like!\n\n")
    input("Continue...")
