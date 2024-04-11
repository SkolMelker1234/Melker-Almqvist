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
riddle6 = """Oft I must strive with wind and wave, Battle them both when under the sea
I feel out the bottom, a foreign land. In lying still I am strong in the strife;
If I fail in that they are stronger than I, And wrenching me loose, soon put me to rout.
They wish to capture what I must keep. I can master them both if my grip holds out,
If the rocks bring succor and lend support, Strength in the struggle. Ask me my name!"""
answer6 = ["anchor", "an anchor"]

riddle_list = {
    riddle1 : answer1,
    riddle2 : answer2,
    riddle3 : answer3,
    riddle4 : answer4,
    riddle5 : answer5,
    riddle6 : answer6
}


def riddle():
    rid, key = rand.choice(list(riddle_list.items()))
    return rid, key

def check_answ(key):
    i = 0
    while i <=1:
        inp = input("->").lower()
        if inp == key[0] or inp == key[1]:
            return "correct"
        elif i < 1:
            print("Try again")
            i += 1
        else:
            i += 1   
    return "incorrect"
