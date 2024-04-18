import random as rand


def play():
    rps_lst = ["r", "p", "s"]
    while True:
        inp = input(f"Rock(r), Paper(p) or Scissors(s)?\n")
        enemy = rand.choice(rps_lst)
        if inp.lower() == "r":
            if enemy == "s":
                print("You win")
                return "You win"
            elif enemy == "r":
                print("play again")
                continue
            else:
                print("You lost")
                return "You lost"
        
        elif inp.lower() == "p":
            if enemy == "s":
                print("You lost")
                return "You lost"
            elif enemy == "r":
                print("play win")
                return "You win"
            else:
                print("Play again")
                continue
        else:
            if enemy == "s":
                print("Play again")
                continue
            elif enemy == "r":
                print("You lost")
                return "You lost"
            else:
                print("You win")
                return "You win"
