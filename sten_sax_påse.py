import random

def sten_sax_pase():
    choices = {
        "sten": "🪨",
        "sax": "✂️",
        "påse": "📄"
    }

    # Förkortningar för enklare input
    shortcuts = {
        "s": "sten",
        "x": "sax",
        "v": "påse"
    }

    print("Välkommen till spelet Sten-Sax-Påse! 🪨 ✂️ 📄")
    print("Spelet pågår tills du vinner eller förlorar.")
    print("Förkortningar: S = sten, X = sax, V = påse")

    while True:
        # Spelarens val
        player_input = input("Välj sten (🪨), sax (✂️) eller påse (📄): ").lower()

        # Kolla om det är en förkortning
        if player_input in shortcuts:
            player = shortcuts[player_input]
        elif player_input in choices:
            player = player_input
        else:
            print("Ogiltigt val, försök igen! Använd sten/sax/påse eller S/X/V")
            continue

        # Datorns val
        computer = random.choice(list(choices.keys()))
        print(f"Du valde: {choices[player]} ({player})")
        print(f"Datorn valde: {choices[computer]} ({computer})")

        # Avgör resultatet
        if player == computer:
            print("Oavgjort! Försök igen...\n")
            continue
        elif (
            (player == "sten" and computer == "sax") or
            (player == "sax" and computer == "påse") or
            (player == "påse" and computer == "sten")
        ):
            print("Grattis, du vann! 🎉")
            break
        else:
            print("Tyvärr, du förlorade. 😢")
            break


if __name__ == "__main__":
    sten_sax_pase()
