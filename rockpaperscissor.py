import random
def play():
    rps_lst = ["r", "p", "s"]
    while True:
        inp = input(f"Rock(r), Paper(p) or Scissors(s)?\n-> ")
        if inp not in rps_lst:
            print("Wrong input silly human")
            continue
        enemy = random.choice(rps_lst)
        
        if inp.lower() == enemy:
            print("Tie, try again")
            continue
        elif inp == "r" and enemy == "s" or inp == "s" and enemy == "p" or inp == "p" and enemy == "r":
            return "You win"
        else:
            return "You lost"
        
