import random

def game():
    print("You are playing a game")
    score = random.randint(1, 62)

    try:
        with open("hiscore.txt") as f:
            hiscore_str = f.read()
            if hiscore_str.strip() != "":
                hiscore = int(hiscore_str.strip())
            else:
                hiscore = 0
    except FileNotFoundError:
        hiscore = 0

    print(f"Your score: {score}")
    if score > hiscore:
        print("Congratulations on the new high score!")
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
        return score
    else:
        print(f"The current high score is: {hiscore}")
        return hiscore

game()
