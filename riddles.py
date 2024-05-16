import random as rand

riddle_dict = {
    "I'm always hungry, I must always be fed. The finger I touch, will soon turn red. What am I?" : ["fire", "a fire"],

    "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?" : ["echo", "an echo"],

    "The more you take, the more you leave behind. What am I?" : ["footsteps", "footstep"],

    "What’s a knight’s favorite type of music?" : ["metal", "heavy metal"],

    "Why did the blacksmith have trouble sleeping at night?" : ["knightmares", "knight mares"],

    "I’m a heavy metal object, dropped to the sea floor, keeping ships in place." : ["anchor", "an anchor"],

    "The more of this there is, the less you see. What is it" : ["darkness", "the darkness"],

    "I speak without a mouth and hear without ears. I have no body, but I come alive with light. What am I?" : ["an image", "a reflection", "image", "reflection"],

    "I'm not alive, but I can grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?" : ["fire", "a flame"], 

    "I have cities, but no houses. I have forests, but no trees. I have rivers, but no water. What am I?" : ["a map", "a world map", "map", "world map"],

    "What runs around the whole yard without moving?" : ["a fence", "a perimeter", "fence"],

    "What has a neck but no head?" : ["a bottle", "a jar", "bottle", "jar"],

    "What has keys but can't open locks?" : ["a piano", "piano"], 

    "The person who makes it, sells it. The person who buys it, never uses it. The person who uses it, never knows they're using it. What is it?" : ["a coffin", "coffin", "coffins"],

    "I am not alive, but I can die. What am I?" : ["a candle", "candle", "candles"], 
    
    "I can be cracked, made, told, and played. What am I?" : ["a joke", "joke", "jokes"]
}


def riddle():
    rid, key = rand.choice(list(riddle_dict.items()))
    return rid, key

def check_answ(key):
    i = 0
    while i <=1:
        inp = input("-> ").lower()
        if inp in key:
            return "correct"
        elif i < 1:
            print("Try again")
            i += 1
        else:
            i += 1   
    return "incorrect"
