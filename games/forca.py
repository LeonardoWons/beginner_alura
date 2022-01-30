from os import system
import random

def jogar():

    system("cls")

    mensage()

    secret_world = random_secret_world()

    letter_hit = ["_" for i in secret_world]
    print("The size world is:")
    print(letter_hit)

    win = False
    die = False
    life = 6

    while(not die and not win):

        kick = input("What letter?")
        kick = kick.strip().upper()

        if(kick in secret_world):
            i = 0
            for letter in secret_world:
                if(kick == letter):
                    letter_hit[i] = letter

                i += 1 
        
        else:
            life -= 1
            print("You miss, you have {} life's".format(life))

        print(letter_hit)

        die = life == 0
        win = "_" not in letter_hit
    
    if(win):
        winner()

    elif(win == False):
        print("You lose, baka")

    
    print("END GAME")



def winner():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def loser(secret_world):
    print("You lose, baka")
    print("The world is {}".format(secret_world))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def mensage():

    print("*********************************")
    print("**** Welcome to gallows game ****")
    print("*********************************")


def random_secret_world():
    with open("worlds.txt", "r") as file:
        worlds = []
        
        for line in file:
            line = line.strip()
            worlds.append(line)

    number = random.randrange(0, len(worlds))
    secret_world = worlds[number].upper()
    return secret_world

if(__name__ == "__main__"):
    jogar()