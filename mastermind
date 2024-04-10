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
"""
    Här checkar vi ifall gissningen inkluderar nummer utanför range(1, 7) 
    Ifall den är utanför så returnar funktionen False och man får skriva in igen. 
    Om man också har skrivit en bokstav så returnerar funktionen också False och gör att man behöver skriva igen.
    """

def inputcheck(alternativ_1, alternativ_2, intake):
    return intake.lower() == alternativ_1 or intake.lower() == alternativ_2
"""
    Här kollar vi om inmatningen är lika med antingen alternativ 1 eller 2. 
    Exempelvis ifall man ska skriva antingen ja eller nej och man inmatar "b" så ber koden en mata in igen, men annars returnerar den True.
    """

def hard(): #Klar
    return [str(rand.randint(1, 6)) for _ in range(4)]
"""
Här gör vi en lista med 4 nummer mellan 1 och 6.
Vi returnarar nummrerna som strings i en lista.
Eftersom den svåra ska kunna repetera nummer så skriver vi bara rand.randint(1,6).
Vilket innebär att rangean inte minskar och den kan råka ta samma slumptal.
"""

def easy(): #Klar båda är strings i en lista
    urn = list(range(1, 7))
    rand.shuffle(urn)
    return [str(urn.pop()) for _ in range(4)]
"""
Den returnerar nummer som strings i en lista här också.
Här ska den dock inte repetera nummer så vi gör en urna och shufflear den.
Sen poppar den ut nummer ur urnan fyra gånger.
Eftersom pop tar bort värden så kan inte nummer repeteras.
"""

def difficulty():#Klar
    while True:
        print("Välj svår eller lätt")
        val = str(input("Välj -> "))
        if val.lower().replace(" ", "") == "svår":
            return hard()
        #Här anropas funktionen svår och då får variabeln kombination värdet som svår skapar
        elif val.lower() == "lätt":
            return easy()
        #fungerar liknande som den ovanför
        else:
            print(f"\n{Colors.error + Colors.bold}Fel inmatning!\n{Colors.endc}")
        #Ifall inmatningen inte motsvarar någon av nummrerna så kommer den skriva ut fel inmatning med röd text.

def gui(guesses, feedback):
    print(f"\n  {Colors.title + Colors.bold}Drag #         Drag          Feedback{Colors.endc}")
    print(f"{Colors.border + Colors.bold}------------------------------------------{Colors.endc}")
    for i in range(12):
        print(f"\n{Colors.text}{(12 - i):5.0f}         {guesses[12 - (i + 1)]}         {feedback[12 - (i + 1)]}{Colors.endc}")
    #Skriver ut talen från 12 till 1 och sen feedbacken för just den omgången anropas och skrivs ut
    print(f"\n{Colors.border + Colors.bold}------------------------------------------{Colors.endc}")

def intake(amount, guesses):
    while True:
        player_guess = (input("\nGissa -> ")).replace(" ", "")
        correct_numbers = numbers(player_guess)
        #här kollar den om nummrerna i input spel_giss faktiskt är mellan 1-6 samt om de är nummer.
        if len(player_guess) != 4:
            print(f"{Colors.error + Colors.bold}\nMåste vara fyra siffror{Colors.endc}")
            """
            Här kollar den om det är fyra siffror som har skrivits.
            Om det inte är så kommer den skriva ut att det måste vara fyra siffror med röd fetstil text.
            """
        elif correct_numbers is True:
            guesses[amount] = player_guess.replace("", " ")
            return player_guess
            #Den här returnerar spelarens gissning om det bara är siffror mellan 1-6 i gissningen.
        else:
            print(f"{Colors.error + Colors.bold}\nMåste vara siffror mellan 1 till 6{Colors.endc}")

def guess():
    guesses = ["", "", "", "", "", "", "", "", "", "", "", ""]
    feedback = ["", "", "", "", "", "", "", "", "", "", "", ""]
    amount_guesses = 0
    combination = difficulty()
    #Här anropas funktionen difficulty så vi får en kombination man ska försöka gissa sig till.
    while True:
        removed = 0
        """
        För varje rätt nummer på antingen fel plats eller rätt plats blir removed ett tal högre än 0.
        Detta görs så att rätt nummer tas bort från tal listan
        """
        resultat = []
        combination_copy = combination.copy()
        #listan combination_copy får alla kombinationens nummer i sig dvs blir kopierad

        if amount_guesses == 12:
            print(f"Inga fler gissningar!\nRätt kombination var: {' '.join(combination)}")
            break
        #Här skrivs listan kombination ut som ett kombinerat nummer med mellanrum.

        player_guess = intake(amount_guesses, guesses)

        for i in range(len(combination)):
            if player_guess[i] == combination[i]:
                resultat.append("✔")
                combination_copy.pop(i - removed)
                removed += 1
            """
            Här kollar den om spelarens gissning är rätt för varje nummer spelaren gissat.
            Ifall nummret finns i kombinationen och är på rätt plats ✔ in i resultatet.
            Sen tas just det talet bort från listan tal så att inte resultatet skrivs ut fel senare i for loopen under. 
            """

        for i in range(len(player_guess)):
            if player_guess[i] in combination_copy and player_guess[i] != combination[i]:
                resultat.append("❐")
                combination_copy.remove(player_guess[i])
                """
                Ifall det gissade nummret är i listan tal 
                dvs inte helt borttaget ovanför och det gissade nummret inte är på samma plats som kombinationen 
                dvs rätt nummer rätt plats så skrivs ❐ in i resultatet och listan tal blir av med det gissade nummret.
                """

        feedback[amount_guesses] = " ".join(resultat)

        gui(guesses, feedback)
        #resultatet och feedbacken skrivs ut.

        if list(player_guess) == combination:
            print("\nGrattis, du har gissat rätt!")
            return True
        #ifall man skrev rätt så avslutas hela funktionen

        amount_guesses += 1
        #man kan bara gissa 12 gånger sen är spelet över

def info():
    kört_innan = input("Behöver du information om hur spelet funkar (ja/nej) -> ")
    while not inputcheck("ja", "nej", kört_innan):
        #När inputcheck() returnerar True så avbryts loopen
        if inputcheck("ja", "nej", kört_innan) is False:
            print(f"\n{Colors.error + Colors.bold}Fel inmatning!{Colors.endc}")
        #Om det man har skrivit in inte är 'ja' eller 'nej' så kommer koden säga att det är fel inmatning
        kört_innan = input("\nJa eller nej -> ")
    return kört_innan.lower().replace(" ", "") == "ja"
"""
Ifall koden är ja kommer informationen att skrivas ut eftersom den returnerar True.
Annars skrivs informationen om spelet inte ut eftersom den returnerar False.
"""


def play():
    if info() is True:
        print(f'''{Colors.explanation} 
        Puzzlemaster kommer att slumpa fram en kod mellan 1 och 6.
        Du ska försöka gissa denna kods siffror på max 12 drag
        Efter respektive gissning så kommer du få en respons: 
        För varje korrekt gissad siffra på rätt plats plats i koden: ✔
        För varje korrekt gissad siffra på fel plats i koden: ❐
        För de siffror som inte finns i koden ges ingen markering.

        Du får välja mellan två svårighetsgrader:
        Lätt: alla siffror i koden är olika
        Svårt: det kan finnas upprepningar av en eller flera siffror
        {Colors.endc}''')
        #Texten skrivs ut med magenta färg
    while True:
        guess()
        igen = False
        if igen is False:
            print("Programmet avslutades normalt")
            break
        #Om man inte vill köra igen avbryts hela loopen och programmet avslutas

play()
#här startas spele
