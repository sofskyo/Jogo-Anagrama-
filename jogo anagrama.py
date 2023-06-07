import json
import random

# Abrir o arquivo JSON
file = open("dictionary.json")
data = json.load(file)

# Colocar as chaves do dicionário em uma lista
dicionario = list(data.keys())

# Pontuação inicial
pontos = 0

print("---------- Welcome to the ANAGRAM game! ----------\n                ~(˘▾˘~)(~˘▾˘)~")
print("")

def jogo(aleatorio):
    global pontos
    recomecar = False
    again = False
    tentativas = 5
    while True:
        print("Here's a hint: \n {}".format(data[aleatorio]))
        print("")
        resposta = ""
        while resposta != aleatorio:
            print("Attempts Left: " + str(tentativas))
            resposta = input("Your guess: ")
            tentativas -= 1
            if tentativas == 0 or resposta == "1":
                again = True
                break
        print("")
        if resposta == "1":
            print("----------- GAME OVER -----------\n        (╯°□°）╯︵ ┻━┻\nThe response was {}".format(aleatorio))
            break
        elif resposta == aleatorio:
            pontos += 1
            print("Correct! The original word was {}! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧".format(aleatorio))
            again = True
            print("Current score: {}".format(pontos))
            print("")
        if again:
            escolha = input("If you want to continue playing, press 'y' for yes or 'n' for no: ")
            print("")
            print("--------------------------------------------------------------------")
            print("")
            while escolha.lower() != "n" and escolha.lower() != "y":
                print("")
                print("You can only choose 'y' or 'n'! (´≖ ‸ ≖)")
                escolha = input("If you want to continue playing, press 'y' for yes or 'n' for no: ")
            if escolha.lower() == "n":
                print("")
                print("Thank you for playing! (✿ ◕‿◕)و ̑̑♡")
                break
            elif escolha.lower() == "y":
                recomecar = True
                break
    if recomecar:
        denovo()

def denovo():
    global pontos
    # Escolhe uma palavra aleatoriamente
    nivel = input("Choose the difficulty level (easy/medium/hard): ")
    while nivel.lower() != "easy" and nivel.lower() != "medium" and nivel.lower() != "hard":
        print("Invalid difficulty level! Please choose 'easy', 'medium', or 'hard'.")
        nivel = input("Choose the difficulty level (easy/medium/hard): ")

    if nivel.lower() == "easy":
        aleatorio = random.choice(dicionario[:500])
    elif nivel.lower() == "medium":
        aleatorio = random.choice(dicionario[500:1000])
    else:
        aleatorio = random.choice(dicionario[1000:])

    # Embaralhar as letras da palavra
    st = list(aleatorio)
    random.shuffle(st)
    l2 = "".join(st)
    print("-Solve the original word for this anagram: {}".format(l2))
    print("-If you want to give up, please press '1'! (ಥ_ಥ)")
    print("")
    jogo(aleatorio)

denovo()
