#Kod för äventyrsspel
import random as random


class Colors:
    remove = "\u001b[0m" #Tar bort färg och annat
    bold = "\u001b[1m" #Fetstil
    red = "\u001b[31m" #Röd
    green = "\u001b[32m" #Grön
    yellow = "\u001b[33m" #Gul
    blue = "\u001b[34m" #Blå
    purple = "\u001b[35m" #Lila
    cyan = "\u001b[36m" #Cyan
    

class Monster:
    def __init__(self, name, STR, HP):
        self.name = name
        self.STR = STR
        self.HP = HP
    
    def fight(self, player):
        while self.HP > 0:
            input("Press enter to hit the monster!")
            roll = random.randint(1, 20)
            if roll == 20:
                print(f"{Colors.bold}Critical hit!{Colors.remove}")
                self.HP = 0
            else:
                damage = player.STR * roll
                print(f"{self.name} took {Colors.red}{damage} damage!{Colors.remove}")
                self.HP -= damage
                print(f"{self.HP} HP left!")


            print(f"{Colors.red}You took {damage} damdage{Colors.remove}")
            damage = random.randint(1, 20) * self.STR
            player.HP -= damage
            if player.HP < 1:
                game_over()
        
        print(f"{self.name} died!")
        player.lvl += 1
        print(f"{Colors.bold}Level up!{Colors.remove}")
                

monsterlst = [Monster("Chompy", 2, 10), Monster("Elgnoblin", 3, 20), Monster("Pissbat", 1, 1), Monster("Borkorc", 5, 50), Monster("Karkus", 1, 50), Monster("Hästjesper", 3, 70), Monster("Puzzlemaster", 20, 200)]


def game_over():
    print(f"{Colors.bold + Colors.red}Game over...{Colors.remove}")
    exit()


class Player:
    def __init__(self):
        self.HP = 50
        self.max_HP = 50
        self.STR = 2
        self.LVL = 1
        self.inv = []
        self.inv_size = 2

    def remove_from_inv(self, item):
        self.inv.remove(item)
        if item.type == "S":
            self.STR -= item.bonus
    
    def remove_from_inv_menu(self):
        self.display_inv()
        inp = input("What do you want to remove?")
        for item in self.inv:
            if item.name.lower() == inp.lower():
                self.remove_from_inv(item)
        
    def add_to_inv(self, item):
        if len(self.inv) == self.inv_size:
            while True:
                inp = input("Inventory full, do you want to remove something? (y/n) ->")
                if inp.lower() == "y":
                    self.remove_from_inv_menu()
                elif inp.lower() == "n":
                    return 1
                
        self.inv.append(item)
        if item.type == "S":
            self.STR += item.bonus

    def display_inv(self):
        print(f"\nInventory")
        print("-----------")
        if len(self.inv) > 0:

            for i in self.inv:
                print(i.name, i.bonus)
                print()
        else:
            print("Empty")

        
    def stats(self):
        print(f"{Colors.bold}Stats")
        print("-----------")
        print(f"""
Your HP is {self.HP}/{self.max_HP}
You are level {self.LVL}
Your strength is {self.STR}
Your inventory has {self.inv_size} slots{Colors.remove}""")
            

# alla items har ett namn, en typ, S för styrkeboostande och H för healing
# bonus är hur mycket de boostar styrka/hp
class Item:
    def __init__(self, name, type, bonus):
        self.name = name
        self.type = type
        self.bonus = bonus
    
    def use(self, player):
        if self.type != "H":
            return "You can't use this item"
        if player.HP == player.max_HP:
            return "You're already at max HP"
        player.HP += self.bonus
        if player.HP > player.max_HP:
            player.HP = player.max_HP
        player.remove_from_inv(self)


itemlist = [Item("Wooden sword", "S", 1), Item("Stone sword", "S", 2), Item("Diamond sword", "S", 4), Item("Healing potion", "H", 3), Item("Good healing potion", "H", 6), Item("Legendary healing potion", "H", 9)]
shit_itemlist = [Item("Stone", "", 0), Item("String", "", 0), Item("Stick", "", 0,), Item("Bone", "", 0), Item("Rotten leg", "", 0), Item("Paper", "", 0)]


def chest_loot():
    chest_inv = []
    num_item = random.randint(1,3)
    for _ in range(num_item):
        loot = random.choice([itemlist, shit_itemlist])
        chest_inv.append(random.choice(loot))
    
    return chest_inv


def puzzle_chest():
    i = 0
    print("It's a puzzle chest, you have to complete the puzzle in order to get the treasure!")
    #Riddel ska importeras
    print("Riddle")
    while i >= 1:
        inp = input("->")
        if inp == 0: #riddle_key
            print(f"{Colors.green}Congratulations traveler you solved the puzzle{Colors.remove}")
            chest_loot()   
        else:
            print(f"Sorry you {Colors.red}faild{Colors.remove} the puzzle, try again!")
        i += 1
    else:
        print(f"{Colors.red}You failed the puzzle, the chest exploded and you took some damage.{Colors.remove}")
        player.hp -= 5
        print(f"Your new HP is:{player.HP}")
    return


def creat_chest():
    #nor = 100-10
    #Puzz = 9-0
    roll_puzz = 100 #random.randint(0, 100)
    if roll_puzz >= 10:
        return chest_loot()
    else:
        return puzzle_chest() 


def generate_room():
    #Monster 100-60
    #Kista 59-20
    #Fälla 19-0
    
    ran_num = (random.randint(0, 100))

    if 100>= ran_num >=5:
        monster_room()
    elif 2>= ran_num >=1:
        chest_room()
    elif 4>= ran_num >=3:
        trap_room()
    return


def monster_room():
    mon = random.choice(monsterlst)
    mon.fight(player)
    

def chest_room(): 
    print("You walked in to a chest room!")
    chest_inv = creat_chest()
    while True:
        i = 0
        print("What item do you want to take?")
        if len(chest_inv) == 0:
            return
        
        for item in chest_inv:
            print(f"{i+1}: {item.name}")
            i += 1
        print(f"{i+1}: Done")

        while True:
            try:
                inp = int(input("->"))-1
                if inp in range(0, i+1):
                    break
            except ValueError:
                print("Can't type that number idot")
                
        if inp == i:
            return
        
        else:
            if player.add_to_inv(chest_inv[inp]) != 1:
                chest_inv.pop(inp)
      

def trap_room():
    print("A trap suddenly activates")
    input("Press enter to avoid")
    roll = random.randint(1,20)
    if (roll + player.STR) >= 15:
        print("You narrowly avoid the trap before you")
    else:
        print(f"{Colors.red}You fall into the trap and take damage{Colors.remove}")
        player.HP = player.HP - 1
        print(f"your HP is now {player.HP}")
    return 


def choose_room():
    print("""Behind one of these doors lies treasure
Behind another lies a monster
Behind the last one lies a trap
Choose wisely between (left), (middle) and (right) traveler""")
    while True:   
        chose = input("->").lower()
        if chose in ["left", "middle", "right"]:
            generate_room()
            return
        else:
            print("You can not read nor type L")


player = Player()
while True:
    print("""
What do you want to do?
1. Choose a room
2. See your stats
3. See your inventory""")
    inp = int(input("->"))
    if inp == 1:
        choose_room()
    elif inp == 2:
        player.stats()
    elif inp == 3:
        player.display_inv()

    elif inp == 4:
        player.add_to_inv(itemlist[3])
        player.display_inv()
        player.inv[0].use(player)
        player.display_inv()
        player.stats

    else:
        print("You can not read nor type L")
