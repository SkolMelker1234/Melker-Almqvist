import random as rand

riddle1 = "I'm always hungry, I must always be fed. The finger I touch, will soon turn red. What am I?"
answer1 = ["fire", "a fire"]

riddle2 = "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?"
answer2 = ["echo", "an echo"]

riddle3 = "The more you take, the more you leave behind. What am I?"
answer3 = ["footsteps", "footstep"]

riddle4 = "What’s a knight’s favorite type of music?"
answer4 = ["metal", "heavy metal"]

riddle5 = "Why did the blacksmith have trouble sleeping at night?"
answer5 = ["knightmares", "knight mares"]

riddle6 = "I’m a heavy metal object, dropped to the sea floor, keeping ships in place."
answer6 = ["anchor", "an anchor"]

riddle7 = "The more of this there is, the less you see. What is it"
answer7 = ["darkness", "the darkness"]

riddle8 = "I speak without a mouth and hear without ears. I have no body, but I come alive with light. What am I?"
answer8 = ["an image", "a reflection", "image", "reflection"]

riddle9 = "I'm not alive, but I can grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?"
answer9 = ["fire", "a flame"]

riddle10 = "I have cities, but no houses. I have forests, but no trees. I have rivers, but no water. What am I?"
answer10 = ["a map", "a world map", "map"]

riddle11 = "What runs around the whole yard without moving?"
answer11 = ["a fence", "a perimeter", "fence"]

riddle12 = "What has a neck but no head?"
answer12 = ["a bottle", "a jar", "bottle", "jar"]

riddle13 = "What has keys but can't open locks?"
answer13 = ["a piano", "piano"]

riddle14 = "I fly without wings. I cry without eyes. What am I?"
answer14 = ["cloud", "a cloud", "clouds"]

riddle15 = "The person who makes it, sells it. The person who buys it, never uses it. The person who uses it, never knows they're using it. What is it?"
answer15 = ["a coffin", "coffin", "coffins"]

riddle16 = "I am not alive, but I can die. What am I?"
answer16 = ["a candle", "candle", "candles"]

riddle17 = "I can be cracked, made, told, and played. What am I?"
answer17 = ["a joke", "joke", "jokes"]

riddle_dict = {
    riddle1 : answer1,
    riddle2 : answer2,
    riddle3 : answer3,
    riddle4 : answer4,
    riddle5 : answer5,
    riddle6 : answer6,
    riddle7 : answer7,
    riddle8 : answer8,
    riddle9 : answer9, 
    riddle10 : answer10,
    riddle11 : answer11,
    riddle12 : answer12,
    riddle13 : answer13, 
    riddle15 : answer15, 
    riddle16 : answer16, 
    riddle17 : answer17
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
