import random as rand



class Trap:
    def __init__(self, name, text, DMG):
        self.name = name
        self.text = text
        self.DMG = DMG

    


trap_lst = [Trap("Undead Door Mimic", "You walk in to the room and find another door, what could be behind it?", rand.randint(1,20)),
            Trap("Slippery Slime", "You walk through the door and slip on some slime!", rand.randint(1,5)),
            Trap("Arrow Launcher", "You open the door and an arrow comes right at you!", rand.randint(5,25)),
            Trap("Swinging Blades", "You carefully walk in to the room and see three new doors. You take a fewe more steps but the big sword blades starts to swing!.", rand.randint(8,15))]

            
            

def get_trap():
    trap = rand.choice(trap_lst)
    return trap
    
