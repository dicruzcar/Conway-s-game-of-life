from lifegame import LifeGame
from GUI import GUI

if __name__ == "__main__":

    option = ""

    while (option != "G") or (option != "G"):
        option = input("Execute on console or gui? (c/g) :")
        option = option.upper()
        if option == "G":
            GUI(base_unit = 5)
            print("Bye")
        elif option == "C":
            LifeGame(80, 10)
            print("Bye")
