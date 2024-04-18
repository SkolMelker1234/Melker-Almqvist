import random
import os
import sys
import riddles
import mastermind
import rockpaperscissor


class Colors:
    remove = "\u001b[0m" #Tar bort färg och annat
    bold = "\u001b[1m" #Fetstil
    red = "\u001b[31m" #Röd
    green = "\u001b[32m" #Grön
    yellow = "\u001b[33m" #Gul
    blue = "\u001b[34m" #Blå
    purple = "\u001b[35m" #Lila
    cyan = "\u001b[36m" #Cyan
 
   
class Player:
    def __init__(self):
        self.name = "traveler"
        self.HP = 50
        self.max_HP = 50
        self.STR = 2
        self.LVL = 1
        self.inv = []
        self.inv_size = 2

    def reset(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def remove_from_inv(self, item):
        self.inv.remove(item)
        if item.type == "S":
            self.STR -= item.bonus
    
    def remove_from_inv_menu(self):
        found_item = False
        items_to_remove = []
        while True:
            self.display_inv()
            inp = input("What do you want to remove? ").lower() 
            for item in self.inv:
                if item.name.lower() == inp:
                    items_to_remove.append(item)
                    found_item = True
                    break
            if found_item == True:
                for items in items_to_remove:
                    self.remove_from_inv(items)
                    return
            else:
                print("You foolishly claim to own something which you do not")
            
        
    def add_to_inv(self, item):
        if len(self.inv)>= self.inv_size:
            
            while True:
                inp = input("Your bag is filled Traveler, do you wish to remove something? (y/n) -> ")
                if inp.lower() == "y":
                    self.remove_from_inv_menu()
                    break
                elif inp.lower() == "n":
                    return 1
                else:
                    print(f"Invalid input {player.name}")
                    continue
            
                
        self.inv.append(item)
        print(f"{item.name} added to your inventory")
        if item.type == "S":
            self.STR += item.bonus
            print(f"Strength increased by {item.bonus}")

    def use_item(self):
        print("What item do you want to use?")
        inp = input("->").lower()
        for item in self.inv:
            if item.name.lower() == inp.lower() and item.type == "H":
                if self.HP + item.bonus < self.max_HP:
                    self.HP += item.bonus
                    print(f"{Colors.green}you feel your vigour returning, HP is now {Colors.red + self.HP}{Colors.remove}")
                    self.inv.remove(item)
                else:
                    self.HP = self.max_HP
                    print(f"you feel your vigour returning, HP is now {self.HP}")
                    self.inv.remove(item)
            
            pass

    def display_inv(self):
        print(f"\nInventory")
        print("-----------")
        if len(self.inv) > 0:
            for item in self.inv:
                if item.bonus != 0:
                    if item.type == "H":
                        print(f"{item.name} {Colors.green}  {item.bonus} {Colors.remove}")
                    else:
                        print(f"{item.name} {Colors.red}  {item.bonus}  {Colors.remove}")
                else:
                    print(item.name)
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


class Monster:
    def __init__(self, name, STR, HP):
        self.name = name
        self.STR = STR
        self.HP = HP
        self.maxHP = HP

    
    def fight(self, player):
        self.HP = self.maxHP
        if self.name == "Hästjesper":
            print(f"You encounter a wild Hästjesper with {self.HP} HP it charges at you like a mad donkey, fight for your life")
        elif self.name == "Karcus":
            print(f"You meet the illustrous Karcus with {self.HP} HP, it is very weak and very stupid, but beware it questions can kill time itself...")
        else:
            print(f"You encounter a fierce {self.name} with {self.HP} HP, fight for your life or be slayn!")
            while True:
                input("Press enter to hit the monster!")
                roll = random.randint(1, 20)
                if roll == 20:
                    print(f"{Colors.bold}Critical hit!{Colors.remove}")
                    self.HP = 0
                else:
                    damage = player.STR * roll
                    print(f"{self.name} took {Colors.red}{damage} damage!{Colors.remove}")
                    self.HP -= damage
                if self.HP < 1:
                    print(f"{self.name} died!")
                    player.LVL += 1
                    if player.LVL//2:
                        player.inv_size += 1
                    print(f"{Colors.bold}Level up! You're now level {player.LVL}!{Colors.remove}")
                    self.HP = self.maxHP + random.choice([1, -1, 0, -2, 2])
                    return
                else:
                    print(f"{self.name} has {self.HP} HP left!")

                damage = random.randint(1, 10) * self.STR
                print(f"{Colors.red}You took {damage} damdage{Colors.remove}")
                player.HP -= damage
                if player.HP < 1:
                    game_over()
                print(f"You have {Colors.red}{player.HP} HP{Colors.remove} left!")
                        #Säker inmatning
                inp = input("Do you want to use an item? (y/n) -> ").lower()
                #printar alltid även när man bara vill slänga item
                if inp != "y" or inp != "n":
                    print("You can not write")
                if inp == "y":
                    player.use_item()
      
                
easy_monsters = [Monster("Chompy", 2, 10), Monster("Pissbat", 1, 8), Monster("Smoll Spooder", 3, 5), Monster("Fire breathing salamander", 1, 15), Monster("Fetus Zombie", 0, 2)]
intermediate_monsters = [Monster("Elgnoblin", 3, 20), Monster("Karkus", 1, 50), Monster("Spoooder", 2, 30)]
difficult_monsters = [Monster("Hästjesper", 3, 70), Monster("Borkorc", 5, 50), Monster("Super Spooooder", 4, 60)]
Boss = Monster("Puzzlemaster", 20, 300)

def game_over():
    print(f"{Colors.bold + Colors.red}Game over...{Colors.remove}")
    exit()



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


def start_over():
    print(f"Congratulations on winning the game and defeating the {Colors.bold}Puzzlemaster{Colors.remove}")
    while True:
        inp = input(f"Do you want to play again {player.name}? (y/n) ->").lower()
        if inp in "y" or "n":
            if inp == "y":
                player.reset()
            else:
                print("See you next time traveller!")
                print("The program closed successfully")
                quit()
        else:
            print(f"{Colors.red}Incorrect input try again{Colors.remove}")


def fight_puzzlemaster():
    print("A shining light appears and you get teleported to a grand room.")
    print("In front of you a large figure stands, It was me all along it whispers silently, I was the voice inside your head, and I was the one who brought you to this dungeon to partake in my game")
    print("You have shown yourself worthy")
    print("Do you wanna play a game?")
    inp = input("(y/n) ").lower()
    if inp != "n" or inp != "y":
        if inp == "n":
            print("Have fun playing our game again!")
            player.reset()
    print("")
    print("SO YOU WANT TO CHALLENGE ME!!!!!")
    print("Let the game begin!")
    print("")
    play = rockpaperscissor.play()
    if play == "You win":
        Boss.HP -= 100
        print(f"Puzzlemaster took 100 damage")
        print(f"His new {Colors.red}hp{Colors.remove} is {Colors.red}{Boss.HP}{Colors.remove}")
        print(f"I underestimated you {player.name}, it will not happen again...")
        print("")
    else: 
        player.HP -= 10
        print(f"You lost the game and lost {Colors.red}10 hp{Colors.remove}")
        print(f"Your new {Colors.red}hp{Colors.remove} is: {Colors.red}{player.HP}{Colors.remove}")
        print(f"Not that smart now {player.name}?")
        print("Well I will let you live for now")
        print("But do not be so sure of that next round")
        print("")

        
    print("Now time to move on to my next game")
    print("MASTERMIND!")
    play = mastermind.play()
    if play == "You win":
        Boss.HP -= 100
        print("Puzzlemaster took 100 damage")
        print(f"His new {Colors.red}hp{Colors.remove} is {Colors.red}{Boss.HP}{Colors.remove}")
        print(f"Damn it, you really are a {Colors.bold}MASTERMIND{Colors.remove}")
        print("")

    else: 
        player.HP = 0
        print(f"You lost the game and lost {Colors.red}10 hp{Colors.remove}")
        print(f"Your new {Colors.red}hp{Colors.remove} is: {Colors.red}{player.HP}{Colors.remove}")
        print(f"You spectacularly failed to {Colors.bold}CRACK THE CODE...{Colors.remove}")
        game_over()


    print("Now on to my last game, RIDDLES!")
    print(f"This time you will not beat me {player.name}")
    rid, key = riddles.riddle()
    print(rid)
    answ = riddles.check_answ(key)
    if answ == "correct":
        Boss.HP -= 100
        print("Puzzlemaster took 100 damage!")
        print("")
        
    else:
        player.HP = 0
        print("You could not solve all of his puzzles.")
        print("The Puzzlemaster got bored and smashed you with his mighty intellect")
        game_over()
        
    if Boss.HP <= 0:
        print("You won everything")
    else:
        print(f"I an still {Colors.bold}alive!{Colors.remove}")
        print("You have one last chance!")
        print("Solve this final riddle.")
        print("")
        rid, key = riddles.riddle()
        print(rid)
        print("")
        answ = riddles.check_answ(key)
        if answ == "correct":
            Boss.HP -= 100
            print("Puzzlemaster took 100 damage!")
        else:
            print(f"That was your last chance {player.name}")
            print("Prepare to die!!!")
            game_over()
    if Boss.HP <= 0:
        print("You won everything")
        print('''
Alone, I stand amidst the aftermath of cunning and riddles, the victor in a battle of wits and will. 
Shadows coil and dissipate around me, defeated by the light of my resolve.
The echoes of my footsteps are the only company in this silent chamber, yet within me, the memory of allies and mentors echoes louder still.
With each riddle solved, each obstacle overcome, I forged ahead, fueled by determination and guided by intuition.
My blade, a whisper in the dark, found its mark true, and with each strike, I carved a path through the labyrinth of uncertainty.
Now, as the dust settles and the air grows still, I stand tall, the sole architect of my triumph.
But let it be known, the victory is not mine alone. It is a testament to the resilience of the lone wanderer, the courage of the solitary soul.
To those who stood beside me in spirit, who whispered words of encouragement in the depths of my solitude, I offer my silent gratitude. 
Though our paths may diverge, our destinies intertwined for but a fleeting moment, the memory of our shared journey will endure.
So, with the echoes of victory ringing in my ears and the shadows of doubt banished from my heart, I press onward. 
For the road stretches ever forward, and the challenges that lie ahead are but new riddles waiting to be solved.
Farewell to the darkness that once held sway, and welcome to the dawn of a new adventure. 
Alone, yet undaunted, I march into the unknown, for my spirit is unyielding, and my resolve unwavering.                
              ''')
        start_over()



def chest_loot():
    chest_inv = []
    num_item = random.randint(1,3)
    for _ in range(num_item):
        loot = random.choice([itemlist, shit_itemlist])
        chest_inv.append(random.choice(loot))
    
    return chest_inv


def puzzle_chest():
    print("It's a puzzle chest! In ordet to claim your prize you must complete the riddle inscribed on the chest in order to get the treasure!")
    rid, key = riddles.riddle()
    print(rid)
    answ = riddles.check_answ(key)
    if answ == "correct":
        print(f"{Colors.green}Congratulations traveler you answered correctly, claim your divident and continue on your way{Colors.remove}")
        return chest_loot() 
    else:
        print(f"{Colors.red}You failed the puzzle, the chest spontaniously combusted and you were burned.{Colors.remove}")
        player.HP -= 5
        print(f"You took 5 damadge, you're now at {player.HP} HP")
        return []
        


def creat_chest():
    #nor = 100-10
    #Puzz = 9-0
    roll_puzz = 4 #random.randint(0, 100)
    if roll_puzz >= 10:
        return chest_loot()
    else:
        return puzzle_chest() 


def generate_room():
    #Monster 100-60
    #Kista 59-20
    #Fälla 19-0
    
    rand_num = (random.randint(0, 100))

    if 100>= rand_num >=60:
        monster_room()
    elif 59>= rand_num >=20:
        chest_room()
    elif 19>= rand_num >=0:
        trap_room()
    return


def monster_room():
    possible_monsters = easy_monsters
    if player.LVL > 3:
        possible_monsters += intermediate_monsters
    if player.LVL > 6:
        possible_monsters += difficult_monsters
    if player.LVL > 9:
        possible_monsters += difficult_monsters
    if player.LVL > 10:
        
        if random.randint(1, 3) == 1:
            fight_puzzlemaster()
        
    monster = random.choice(possible_monsters)
    monster.fight(player)
    

def chest_room(): 
    print("You walked into a chest room! Claim your items quickly and proceed...")
    chest_inv = creat_chest()
    while True:
        i = 0
        if len(chest_inv) == 0:
            return
        
        print("What item tempts your hands traveler?")
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
                print(f"Invalid input {player.name}")
                
        if inp == i:
            return
        
        else:
            if player.add_to_inv(chest_inv[inp]) != 1:
                chest_inv.pop(inp)
      

def trap_room():
    print("A trap suddenly activates under your feet, are you quick-footed enough as to not fall to your grave?")
    input("Press enter to avoid")
    roll = random.randint(1,20)
    if (roll + player.STR) >= 15:
        print("You narrowly avoid the trap laid before you")
    else:
        print(f"{Colors.red}You tumble into the trap and spikes impale you{Colors.remove}")
        player.HP = player.HP - random.randint(1,5)
        print(f"your HP is now {player.HP}")
    return 


def choose_room():
    print("""Behind one of these doors lies treasure
Behind another lies a monster
Behind the last one lies a trap
Choose wisely between the (left), (middle) and (right) door traveler""")
    while True:   
        chose = input("->").lower()
        if chose in ["left", "middle", "right"]:
            generate_room()
            return
        else:
            print(f"Invalid input {player.name}")


player = Player()
print("You wake up in a dark and moist dungeon, your head aches and you feel weak...")
namn = input(f"What is your name traveler\n-> ")

player.name = namn
if len(player.name) == 0:
    player.name = "traveler"
print(f"Hello {player.name}.. Have fun in my dungeon *omnious laughter that slowly fades away*")
while True:
    print("""
What do you want to do?
1. Choose a room
2. See your stats
3. See your inventory""")
    inp = (input("->"))
    if str(inp) == "1":
        choose_room()
    elif str(inp) == "2":
        player.stats()
    elif str(inp) == "3":
        player.display_inv()

    elif str(inp) == "4":
        fight_puzzlemaster()
        player.inv.append(random.choice(itemlist))

    else:
        print("You can not read nor type L")
