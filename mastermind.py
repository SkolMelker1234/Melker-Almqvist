import random as rand

class Colors: 
    """
    \u001b är en ANSI escape code och innehåller färger och textstilar ex fetstil. 
    Eftersom vi bara vill ändra färgerna så skriver vi 31 eller andra nummer för att välja färgerna. 
    Om vi hade velat ändra färgerna så skriver vi \u001b[1;31m istället där 1 markerar stilen på texten. 
    och 31m vilken färg, i detta fall motsvarar 31m rött.
    """
    error = "\u001b[31m" #Röd
    title = "\u001b[34m" #Blå
    text = "\u001b[32m" #Grön
    border = "\u001b[33m" #Gul
    endc = "\u001b[0m" #Tar bort färg och fetstil
    explanation = "\u001b[35m" #Magenta
    bold = "\u001b[1m" #Fetstil
    """
    class är lite som en lista där man kan anropa funktionen och sen vilken del. 
    För röd text skriver man Colors.error och då får man ANSI koden vilket motsvarar den färgen.
    """

def numbers(guess):
    lst = list(range(1, 7))
    for digit in guess:
        try: 
            if int(digit) not in lst:
                return False
        except ValueError:
            return False
    return True


def inputcheck(alternativ_1, alternativ_2, intake):
    return intake.lower() == alternativ_1 or intake.lower() == alternativ_2

def hard(): #Klar
    return [str(rand.randint(1, 6)) for _ in range(4)]


def difficulty():#Klar
    while True:
        val = "svår"
        if val.lower().replace(" ", "") == "svår":
            return hard()
        #Ifall inmatningen inte motsvarar någon av nummrerna så kommer den skriva ut fel inmatning med röd text.

def gui(guesses, feedback):
    print(f"\n  {Colors.title + Colors.bold}Moves #         move          Feedback{Colors.endc}")
    print(f"{Colors.border + Colors.bold}------------------------------------------{Colors.endc}")
    for i in range(12):
        print(f"\n{Colors.text}{(12 - i):5.0f}         {guesses[12 - (i + 1)]}         {feedback[12 - (i + 1)]}{Colors.endc}")
    #Skriver ut talen från 12 till 1 och sen feedbacken för just den omgången anropas och skrivs ut
    print(f"\n{Colors.border + Colors.bold}------------------------------------------{Colors.endc}")

def intake(amount, guesses):
    while True:
        player_guess = (input("\nGuess -> ")).replace(" ", "")
        correct_numbers = numbers(player_guess)
        #här kollar den om nummrerna i input spel_giss faktiskt är mellan 1-6 samt om de är nummer.
        if len(player_guess) != 4:
            print(f"{Colors.error + Colors.bold}\nHas to be four numbers{Colors.endc}")

        elif correct_numbers is True:
            guesses[amount] = player_guess.replace("", " ")
            return player_guess
            #Den här returnerar spelarens gissning om det bara är siffror mellan 1-6 i gissningen.
        else:
            print(f"{Colors.error + Colors.bold}\nHas to be numbers between 1 and 6{Colors.endc}")

def guess():
    guesses = ["", "", "", "", "", "", "", "", "", "", "", ""]
    feedback = ["", "", "", "", "", "", "", "", "", "", "", ""]
    amount_guesses = 0
    combination = difficulty()
    #Här anropas funktionen difficulty så vi får en kombination man ska försöka gissa sig till.
    while True:
        removed = 0

        resultat = []
        combination_copy = combination.copy()
        #listan combination_copy får alla kombinationens nummer i sig dvs blir kopierad

        if amount_guesses == 12:
            print(f"No more guesses!\n Correct combination: {' '.join(combination)}")
            break
        #Här skrivs listan kombination ut som ett kombinerat nummer med mellanrum.

        player_guess = intake(amount_guesses, guesses)

        for i in range(len(combination)):
            if player_guess[i] == combination[i]:
                resultat.append("✔")
                combination_copy.pop(i - removed)
                removed += 1


        for i in range(len(player_guess)):
            if player_guess[i] in combination_copy and player_guess[i] != combination[i]:
                resultat.append("❐")
                combination_copy.remove(player_guess[i])


        feedback[amount_guesses] = " ".join(resultat)

        gui(guesses, feedback)
        #resultatet och feedbacken skrivs ut.

        if list(player_guess) == combination:
            print("\nCongratulations, you guessed the code!")
            return True
        #ifall man skrev rätt så avslutas hela funktionen

        amount_guesses += 1
        #man kan bara gissa 12 gånger sen är spelet över

def info():
    kört_innan = input("Do you require information (yes/no) -> ")
    while not inputcheck("yes", "no", kört_innan):
        #När inputcheck() returnerar True så avbryts loopen
        if inputcheck("yes", "no", kört_innan) is False:
            print(f"\n{Colors.error + Colors.bold}Wrong input!{Colors.endc}")
        #Om det man har skrivit in inte är 'ja' eller 'nej' så kommer koden säga att det är fel inmatning
        kört_innan = input("\nJa eller nej -> ")
    return kört_innan.lower().replace(" ", "") == "ja"



def play():
    if info() is True:
        print(f'''{Colors.explanation} 
        Puzzlemaster is going to randomize a code between 1 and 6.
        Your goal is to guess the code in 12 guesses
        After each guess you will get a response:
        For every correct number in the right place: ✔
        For every correct number in the wrong place: ❐
        For the numbers not in the code no mark will be given.
        There may be repetitions of numbers in the code.
        {Colors.endc}''')
        #Texten skrivs ut med magenta färg
    while True:
        if guess() == True:
            return "You win"
        else:
            return "You lost"
        #Om man inte vill köra igen avbryts hela loopen och programmet avslutas

#här startas spele
