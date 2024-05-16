import random
import riddles
import mastermind
import rockpaperscissor
import generate_traps
import resetfile
from time import sleep


# printar text långsamt, speed är av default slow men kan ändras till very_slow om man vill printa ännu långsammare
def slow_print(text, speed="slow"):
    sleep_time = 0.02
    if speed == "very_slow":
        sleep_time = 0.8

    for letter in text:
        print(letter, end="", flush=True)
        sleep(sleep_time)


# för att printa färgad text
#som tidigare förklarat är u001b[ en escape code som pausar terminalen
#sen tar terminalen emot en input t.ex. 31m som motsvarar färg 31 som är röd i denna terminal
#olika terminaler kan ha olika färger assigned till dessa värden så just denna röd är inte en konstant
class Colors:
    remove = "\u001b[0m" #Tar bort färg och annat
    bold = "\u001b[1m" #Fetstil
    red = "\u001b[31m" #Röd
    green = "\u001b[32m" #Grön


# klassen med alla spelarattributer och spelarfunktioner
class Player:
    def __init__(self):
        self.name = ""
        self.HP = 50
        self.max_HP = 50
        self.STR = 2
        self.LVL = 1
        self.inv = []
        self.inv_size = 2


    #I resetfile har jag importat  funktionen call från librariet subprocess
    #Call låter oss starta en python fil, men man kan inte starta samma python programm i samma fil
    #Därför behövdes det anropas en annan fil som "startar om"
    def reset(self):
        resetfile.reset()


    #Tar bort item från inventory och tar bort strength ifall det ges av itemet
    def remove_from_inv(self, item):
        self.inv.remove(item)
        if item.type == "STR":
            self.STR -= item.bonus
    
    
    #Skriver ut ditt inventory och frågar vad man vill ta bort 
    def remove_from_inv_menu(self):
        self.display_inv()
        while True:
            slow_print("What item do you wish to remove?")
            inp = input("-> ").lower()

            for item in self.inv:
                if item.name.lower() == inp:
                    self.remove_from_inv(item)
                    slow_print(f"You threw away your {item.name}\n")
                    return
                
            print("You foolishly claim to own something which you do not")
            print("")


    #Lägger till saker i ditt inventory om det inte är fullt
    def add_to_inv(self, item):
        if len(self.inv)>= self.inv_size:
            
            while True:
                slow_print("Your bag is filled traveler, do you wish to remove something?\n") #Frågar om du vill kasta något 
                inp = input("(y/n) -> ").lower()
                if inp == "y" or inp == "yes":
                    self.remove_from_inv_menu()
                    break
                elif inp == "n" or inp == "no":
                    return "bag_full"
                else:
                    slow_print(f"You failed to answer correctly {player.name}\n")
                
        self.inv.append(item)
        slow_print(f"You put {item.name} in your bag\n")
        if item.type == "STR":
            self.STR += item.bonus #Ger spelaren den STR som itemet har
            slow_print(f"You feel your {Colors.red}strength{Colors.remove} increase by {Colors.red}{item.bonus}{Colors.remove}\n")    
        print("")   


    #Skriver ut det som finns i ditt inventory
    def display_inv(self):
        print(f"\n   Inventory {len(self.inv)}/{self.inv_size}")
        print("------------------")
        if len(self.inv) > 0:
            for item in self.inv:
                if item.type == "Health" or item.type == "STR": 
                    if item.type == "Health":
                        print(f"{item.name} {Colors.green}  {item.bonus} {Colors.remove}")
                    else:
                        print(f"{item.name} {Colors.red} {item.bonus}  {Colors.remove}")
                else:
                    print(item.name)
                print()  
        else:
            print("     Empty")
            return "Empty"


    #Denna funktion gör det möjligt för det att använda items
    def use_item(self):
        slow_print("What item do you wish to consume?")
        while True:
            inp = input("-> ").lower()
            for item in self.inv:
                if item.name.lower() == inp.lower():
                    if item.type == "Health":
                        if self.HP == self.max_HP: #Om du redan är på max HP kan du inte använda ett healing item
                            slow_print(f"You can't use this item since you're already at max HP\n")
                            return
                        else:
                            if self.HP + item.bonus < self.max_HP:
                                self.HP += item.bonus
                            else:
                                self.HP = self.max_HP #Du ska inte kunna ha mer HP än ditt max
                            slow_print(f"{Colors.green}You feel your vigour returning, HP is now {self.HP}{Colors.remove}\n")
                            self.inv.remove(item)
                            return
                    else:
                        slow_print("You can not use that item\n")
                    break
            
            else:
                print("You claim to own something which you do not")


    #Ser om du kan använda något i ditt inventory
    def wish_to_use_item(self):
        healing_item_in_inventory = False
        for item in player.inv:
            if item.type == "Health":
                healing_item_in_inventory = True
    
        if healing_item_in_inventory:
            slow_print("Do you wish to use an item?\n")     
            inp = input("(y/n) -> ").lower()
            if inp == "y" or inp == "yes":
                return True
            elif inp == "n" or inp == "no":
                slow_print("You chose not to do anything\n")
                return False
            else:
                slow_print("The moment escaped you\n")
                return False

    #Skriver ut dina stats
    def stats(self):
        print("")
        print(f"        {Colors.bold}Stats{Colors.remove}")
        print("-------------------")
        print(f"""
Your {Colors.green}HP{Colors.remove} is {Colors.green}{self.HP}/{self.max_HP}{Colors.remove}
You're level {self.LVL}
Your {Colors.red}strength{Colors.remove} is {Colors.red}{self.STR}{Colors.remove}
Your {Colors.bold}inventory{Colors.remove} has{Colors.bold} {self.inv_size} slots{Colors.remove}""")


    #Gör att du kan levela upp och ger dig de förmåner som kommer med detta
    def level_up(self):
        self.LVL += 1
        self.max_HP += 2
        self.HP += 2
        slow_print(f"\n{Colors.bold}Level up! You're now level {self.LVL}!{Colors.remove}\n")
        slow_print(f"Your health increases,{Colors.green} MAX HP{Colors.remove} is now {Colors.green}{self.max_HP}{Colors.remove}\n")
        if self.LVL%3 == 0:
            self.inv_size += 1
            slow_print(f"\nYour bag magically increased in size,{Colors.bold} your inventory space has increased by 1{Colors.remove}\n")


# klassen med alla monsterattributer och monsterfunktioner
class Monster:
    def __init__(self, name, STR, HP):
        self.name = name
        self.STR = STR
        self.maxHP = HP
        self.HP = 0


    #Här kan du slåss mot monster
    def fight(self, player):
        self.HP = self.maxHP + random.randint(-3, 3)
        print("")
        if self.name == "Hästjesper": #Lite extra lore
            print('''

       -""\\
    .-"  .`)     (
   j   .'_+     :[                )      .^--..
  i    -"       |l                ].    /      i
 ," .:j         `8o  _,,+.,.--,   d|   `:::;    b
 i  :'|          "88p;.  (-."_"-.oP        \.   :
 ; .  (            >,%\%\%\   f),):8"          \:'  i
i  :: j          ,;%\%\%:; ; ; i:%\%\%.,        i.   `.
i  `: ( ____  ,-::::::' ::j  [:```          [8:   )
<  ..``'::::8888oooooo.  :(jj(,;,,,         [8::  <
`. ``:.      oo.8888888888:;%\%\%\8o.::.+888+o.:`:'  |
 `.   `        `o`88888888b`%\%\%\%\%88< Y888P""'-    ;
   "`---`.       Y`888888888;;.,"888b."""..::::'-'
          "-....  b`8888888:::::.`8888._::-"
             `:::. `:::::O:::::::.`%\%'|
              `.      "``::::::''    .'
                `.                   <
                  +:         `:   -';
                   `:         : .::/
                    ;+_  :::. :..;;;
                    ;;;;,;;;;;;;;,;;   
                  ''')
            slow_print(f"You encounter a wild Hästjesper with {Colors.green}{self.HP} HP{Colors.remove} it charges at you like a mad donkey, fight for your life\n")
        elif self.name == "Karkus":
            slow_print(f"You meet the illustrous Karkus with {Colors.green}{self.HP} HP{Colors.remove}, it is very weak and very stupid, but beware it questions can kill time itself...\n")
        else:
            slow_print(f"You encounter a fierce {Colors.green}{self.name}{Colors.remove} with {Colors.green}{self.HP} HP{Colors.remove}, fight for your life or be slain!\n")
            print("")
        while True:
            input("Press enter to attack the monster!")
            roll = random.randint(1, 20)
            if roll == 20:
                slow_print(f"{Colors.bold}Critical hit!{Colors.remove}\n")
                self.HP = 0
            else:
                damage = round((player.STR * roll)/(5+(player.STR/2)))
                slow_print(f"{self.name} took {Colors.green}{damage} damage!{Colors.remove}\n")
                self.HP -= damage
            if self.HP < 1:
                slow_print(f"{self.name} was slain!\n")
                print("")
                player.level_up()
                return
            
            else:
                slow_print(f"{self.name} has {Colors.green}{self.HP}/{self.maxHP} HP{Colors.remove} left!\n")
                print("")

            damage = round(random.randint(1, 20) * self.STR/10)
            slow_print(f"{Colors.red}You took {damage} damage{Colors.remove}\n")
            print("")
            player.HP -= damage

            if player.HP < 1:
                game_over()
            slow_print(f"You have {Colors.green}{player.HP} HP{Colors.remove} left!\n")

            if player.wish_to_use_item():
                player.display_inv()
                player.use_item()


#Balanserat! (jk)
easy_monsters = [Monster("Chompy", 3, 14), Monster("Pissbat", 2, 10), Monster("Smoll Spooder", 4, 8), 
                 Monster("Fire breathing salamander", 3, 17), Monster("Zombie Fetus", 2, 9)]
intermediate_monsters = [Monster("Elgnoblin", 6, 20), Monster("Karkus", 4, 25), Monster("Spoooder", 5, 30)]
difficult_monsters = [Monster("Hästjesper", 11, 40), Monster("Borkorc", 10, 45), Monster("Super Spooooder", 12, 40), 
                      Monster("Vampyr Jesper",16 ,55)]
boss = Monster("Puzzlemaster", 20, 300)
    

#Om du dör går man till detta där man kan välja om man vill spela igen eller inte
def game_over():
    slow_print(f"{Colors.bold + Colors.red}Game over...{Colors.remove}\n")
    while True:
        inp = str(input("Do you wish to play again traveler (y/n) "))
        if inp.lower() in ["yes", "y", "1"]:
            player.reset()
        elif inp.lower() in ["no", "n", "2"]:
            print("See you next time traveler!")
            print("The program closed successfully")
            quit()
        else:
            print("Wrong input traveler...")
            continue


# alla items har ett namn, en och en bonus (hur mycket de boostar styrka/hp)
class Item:
    def __init__(self, name, type="None", bonus=0):
        self.name = name
        self.type = type
        self.bonus = bonus


itemlist = [Item("Wooden mallet", "STR", 1),Item("Stone mallet", "STR", 2), Item("Iron axe", "STR", 3), 
            Item("Wooden sword", "STR", 2), Item("Stone sword", "STR", 5), Item("Diamond sword", "STR", 10), 
            Item("Healing potion", "Health", 8), Item("Good healing potion", "Health", 15), 
            Item("Legendary healing potion", "Health", 22), Item("Mashed herbs", "Health", 5), 
            Item("Small bandage","Health", 6), Item("Medium bandage", "Health", 14)]

no_stat_itemlist = [Item("Stone"), Item("String"), Item("Stick",), 
                    Item("Bone"), Item("Rotten leg"), Item("Paper")]


#När spelet har avslutats
def start_over():
    slow_print(f"Congratulations on winning the game and defeating the {Colors.bold}Puzzlemaster{Colors.remove}\n")
    while True:
        inp = input(f"Do you want to play again {player.name}? (y/n) ->").lower()
        if inp in ["yes", "no", "n", "y", "1", "2"]:
            if inp in ["yes", "y", "1"]:
                player.reset()
            else:
                slow_print("See you next time traveler!\n")
                print("The program closed successfully")
                quit()
        else:
            print(f"{Colors.red}Incorrect input, try again{Colors.remove}")


#Här är bossbattlet, det är inte lätt att vinna detta
def fight_puzzlemaster():
    boss.HP = 300
    print("")
    slow_print("A shining light appears and you get teleported to a grand room.\n")
    slow_print("In front of you a large figure stands, it was me all along it whispers silently, I was the voice inside your head, and I was the one who brought you to this dungeon to partake in my game\n")
    slow_print("You have shown yourself worthy\n")
    slow_print("So, do you wanna play a game?\n")
    inp = input("(y/n) ").lower()
    if inp not in ["n", "y", "yes", "no", "1", "2"]: #Inmatningssäker
        print("I'm just assuming you said yes, I might have misheard")
    if inp in ["no", "n", "2"]:
        slow_print("Have fun playing this game again!")
        slow_print("...", "very_slow")
        print("")
        player.reset()

    slow_print("\nSO YOU WANT TO CHALLENGE ME?!?!??!?!\n")
    slow_print("Well, let the game begin!\n")
    play = rockpaperscissor.play() #Här kallar vi på funktionen för att spela rock paper scissor i den filen
    if play == "You win":
        boss.HP -= 100
        slow_print(f"Puzzlemaster took {Colors.remove}100 damage{Colors.remove}\n")
        slow_print(f"His new {Colors.green}HP{Colors.remove} is {Colors.green}{boss.HP}{Colors.remove}\n")
        slow_print(f"I underestimated you {player.name}, it will not happen again...\n")
    else: 
        player.HP -= 15
        slow_print(f"You lost the game and lost {Colors.green}15 HP{Colors.remove}\n")
        if player.HP <= 0:
            game_over()
        else:
            slow_print(f"Your new {Colors.green}HP{Colors.remove} is {Colors.green}{player.HP}{Colors.remove}\n")
        slow_print(f"Not that smart now {player.name}?\n")
        slow_print("Well I will let you live for now\n")
        slow_print("But do not be so sure of that next round\n")

        
    slow_print("Now time to move on to my next game\n")
    slow_print("...", "very_slow")
    print('''
                                                                                                                   
88b           d88                                                                      88                      88  
888b         d888                        ,d                                            ""                      88  
88`8b       d8'88                        88                                                                    88  
88 `8b     d8' 88 ,adPPYYba, ,adPPYba, MM88MMM ,adPPYba, 8b,dPPYba, 88,dPYba,,adPYba,  88 8b,dPPYba,   ,adPPYb,88  
88  `8b   d8'  88 ""     `Y8 I8[    ""   88   a8P_____88 88P'   "Y8 88P'   "88"    "8a 88 88P'   `"8a a8"    `Y88  
88   `8b d8'   88 ,adPPPPP88  `"Y8ba,    88   8PP""""""" 88         88      88      88 88 88       88 8b       88  
88    `888'    88 88,    ,88 aa    ]8I   88,  "8b,   ,aa 88         88      88      88 88 88       88 "8a,   ,d88  
88     `8'     88 `"8bbdP"Y8 `"YbbdP"'   "Y888 `"Ybbd8"' 88         88      88      88 88 88       88  `"8bbdP"Y8  
                                                                                                                   
          ''')
    play = mastermind.play() #startar mastermind i dens fil
    if play == "You win":
        boss.HP -= 100
        slow_print(f"Puzzlemaster took {Colors.green}100 damage{Colors.remove}\n")
        slow_print(f"His new {Colors.green}HP{Colors.remove} is {Colors.green}{boss.HP}{Colors.remove}\n")
        slow_print(f"Damn it, you really are a {Colors.bold}MASTERMIND{Colors.remove}\n")


    else: 
        player.HP = 0 #Om man misslyckas här dör man
        slow_print(f"You lost the game and lost {Colors.green}10 HP{Colors.remove}\n")
        slow_print(f"Your new {Colors.green}HP{Colors.remove} is: {Colors.green}{player.HP}{Colors.remove}\n")
        slow_print(f"You spectacularly failed to {Colors.bold}CRACK THE CODE...{Colors.remove}\n")
        game_over()

    slow_print("Now on to my last game\n")
    slow_print("...", "very_slow")
    print('''

88888888ba  88          88          88 88                       
88      "8b ""          88          88 88                       
88      ,8P             88          88 88                       
88aaaaaa8P' 88  ,adPPYb,88  ,adPPYb,88 88  ,adPPYba, ,adPPYba,  
88""""88'   88 a8"    `Y88 a8"    `Y88 88 a8P_____88 I8[    ""  
88    `8b   88 8b       88 8b       88 88 8PP"""""""  `"Y8ba,   
88     `8b  88 "8a,   ,d88 "8a,   ,d88 88 "8b,   ,aa aa    ]8I  
88      `8b 88  `"8bbdP"Y8  `"8bbdP"Y8 88  `"Ybbd8"' `"YbbdP"'  
          
''')
    slow_print(f"This time you will not beat me {player.name}\n")
    rid, key = riddles.riddle() #Här kallar vi på riddlefilen
    slow_print(rid)
    answ = riddles.check_answ(key)
    if answ == "correct":
        boss.HP -= 100
        slow_print(f"Puzzlemaster took {Colors.green}100 damage{Colors.remove}!\n")

        
    else:
        player.HP = 0 #Här är vi hårda på spelaren igen
        slow_print("You could not solve all of his puzzles.\n")
        slow_print("The Puzzlemaster got bored and smashed you with his mighty intellect\n")
        game_over()
        
    if boss.HP <= 0:
        return True #Om puzzlemaster är dör du vinner
    else:
        slow_print(f"I am still {Colors.bold}alive!{Colors.remove}\n") #Annars får du en sista chans 
        slow_print("You have one last chance!\n")
        slow_print("Solve this final riddle.\n")
        rid, key = riddles.riddle()
        slow_print(rid)
        print("\n")
        answ = riddles.check_answ(key)
        if answ == "correct":
            boss.HP -= 100
            print(f"Puzzlemaster took {Colors.green}100 damage{Colors.remove}!")
        else:
            slow_print(f"That was your last chance {player.name}")
            slow_print("Prepare to die!!!")
            game_over()
    if boss.HP <= 0:
        return True
        

#Fixar loot till kistor
def chest_loot():
    chest_inv = []
    num_item = random.randint(1,3)
    for _ in range(num_item):
        loot = random.choice([itemlist, no_stat_itemlist])
        chest_inv.append(random.choice(loot))
    
    return chest_inv

#Om man får en puzzlekista kommer man hit och får ett riddle
def puzzle_chest():
    slow_print("It's a puzzle chest! In ordet to claim your prize you must complete the riddle inscribed on the chest!!\n")
    rid, key = riddles.riddle()
    print(rid)
    answ = riddles.check_answ(key)
    if answ == "correct":
        slow_print(f"{Colors.green}Congratulations traveler you answered correctly, claim your divident and continue on your way{Colors.remove}\n")
        return chest_loot() 
    else:
        slow_print(f"{Colors.red}You failed the puzzle, the chest spontaniously combusted and you were burned.{Colors.remove}\n")
        player.HP -= 5
        if player.HP < 1:
            game_over()
        print(f"You took {Colors.red}5 damage{Colors.remove}, you're now at {Colors.green}{player.HP} HP{Colors.remove}")
        return []


#Här slumpar den om man får en puzzle eller vanlig kista
def create_chest():
    #nor = 100-10
    #Puzz = 9-0
    roll_puzz = random.randint(0, 100)
    if roll_puzz >= 10:
        return chest_loot()
    else:
        return puzzle_chest() 


#Här slumpar vi fram rum
def generate_room():
    #Monster 0-50
    #Kista 50-80
    #Fälla 80-100
    
    rand_num = (random.randint(0, 100))
    if 0<= rand_num <=50:
        monster_room()
    elif 50< rand_num <=80:
        chest_room()
    elif 80< rand_num <=100:
        trap_room()
    return


#Om man stöter på monster kommer man hit
def monster_room():
    possible_monsters = easy_monsters
    if player.LVL > 3:
        possible_monsters += intermediate_monsters
    if player.LVL > 6:
        possible_monsters += difficult_monsters
    if player.LVL > 9:
        possible_monsters += difficult_monsters
    if player.LVL > 10:
        if random.randint(1, 3) == 1: #Här behöver man har tur för att möte bossen så att man inte automatiskt får bossen
            if fight_puzzlemaster():
                slow_print("You won everything")
                slow_print('''
Alone, you stand amidst the aftermath of cunning and riddles, the victor in a battle of wits and will. 
Shadows coil and dissipate around you, defeated by the light of your resolve.
The echoes of your footsteps are the only company in this silent chamber.
With each riddle solved, each obstacle overcome, you forged ahead, fueled by determination and guided by intuition.
Your blade, a whisper in the dark, found its mark true, and with each strike, you carved a path through the labyrinth of uncertainty.
Now, as the dust settles and the air grows still, you stand tall, the sole architect of your triumph.
But let it be known, the victory is not yours alone. It is a testament to the resilience of you, the lone wanderer, the courage of the solitary soul.
So, with the echoes of victory ringing in your ears and the shadows of doubt banished from your heart, you press onward. 
For the road stretches ever forward, and the challenges that lie ahead are but new riddles waiting to be solved.
Farewell to the darkness that once held sway, and welcome to the dawn of a new adventure. 
Alone, yet undaunted, you march into the unknown, for your spirit is unyielding, and your resolve absolute.''')
                start_over()
        
    monster = random.choice(possible_monsters)
    monster.fight(player)
    

#Om man får en kista kommer man hit    
def chest_room(): 
    print("")
    slow_print("You walked into a chest room! Claim your items quickly and proceed...\n")
    chest_inv = create_chest() #Kallar på funktionen för att lägga saker i kistan
    while True:
        i = 0
        if len(chest_inv) == 0:
            return
        
        slow_print("What item tempts your hands traveler? \n")
        for item in chest_inv: 
            print(f"{i+1}: {item.name}")
            i += 1
        print(f"{i+1}: Done")
        while True:
            try:
                inp = int(input("-> "))-1
                if inp in range(0, i+1):
                    break
                else:
                    print(f"There is only {i} items in this chest")
            except ValueError:
                print(f"Invalid input {player.name}")
                
        if inp == i:
            return
        else:
            if player.add_to_inv(chest_inv[inp]) != "bag_full":
                chest_inv.pop(inp)


#Om du får en fälla kommer du hit      
def trap_room():
    trap = generate_traps.get_trap() #Kallar på funktionen för att generera traps i traps filen
    slow_print(f"{trap.text}\n")   
    input("Press enter to continue\n")
    roll = random.randint(1,20)
    if ((roll + player.STR)/2) >= 10:
        slow_print("You got lucky and avoided the trap laid before you\n") #Lite roligt om man kan undika fällan
    else:
        slow_print(f"{Colors.red}You could not avoid the trap and took some damage{Colors.remove}\n")
        player.HP = player.HP - random.randint(1,5) - trap.DMG #Lite random är roligt
        if player.HP < 1:
            game_over()
        slow_print(f"Your {Colors.green}HP{Colors.remove} is now {Colors.green}{player.HP}{Colors.remove}\n")
    return 


#Här kan du välja rum trotts att det är slumpat
def choose_room():
    print("""
Behind one of these doors lies treasure
Behind another lies a monster
Behind the last one lies a trap
Choose wisely between the (left), (middle) and (right) door traveler""")
    while True:   
        choose = str(input("-> ").lower())
        if choose in ["left", "middle", "right", "1", "2", "3", "l", "m", "r"]:
            generate_room()
            return
        else:
            print(f"You walked face first into wall")


#Spelaren skapas
player = Player()
print("")

#Lite text för att starta spelet
slow_print("You wake up in a dark and moist dungeon, your head aches and you feel weak...\n")
namn = str(input(f"What is your name traveler\n-> ")).replace(" ", "")


#Ger spelaren ett namn
player.name = namn
if len(player.name) == 0:
        player.name = "Nikodesmos"
if player.name == "Gabriel":
    player.add_to_inv(itemlist[5])
    player.add_to_inv(itemlist[8])

#Här kan du välja ad vill du göra
print("")
slow_print(f"Hello {player.name}.. Have fun in my dungeon *omnious laughter that slowly fades away*\n")
while True:
    print("""
~~~~~~~~~~~~~~~~~~~~~~
What do you want to do?
1. Explore the dungeon
2. See your stats
3. Go through your bag""")
    inp = (input("-> "))
    if str(inp) == "1":
        choose_room()
    elif str(inp) == "2":
        player.stats()
    elif str(inp) == "3":
        print("")
        player.display_inv()
        if player.wish_to_use_item():
            player.use_item()

    elif str(inp) == "4":
        if fight_puzzlemaster():
            print("You won...")
            print("You finally won")
            start_over()

    else:
        slow_print("You sat down and wondered how you got here")
        print("")
