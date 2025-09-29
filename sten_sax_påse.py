import random

def sten_sax_pase():
    choices = {
        "sten": "🪨",
        "sax": "✂️",
        "påse": "📄"
    }

    print("Välkommen till spelet Sten-Sax-Påse! 🪨 ✂️ 📄")
    print("Spelet pågår tills du vinner eller förlorar.")

    while True:
        # Spelarens val
        player = input("Välj sten (🪨), sax (✂️) eller påse (📄): ").lower()
        if player not in choices:
            print("Ogiltigt val, försök igen!")
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
