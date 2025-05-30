import random
import time

def lancer_roulette():
    print("🎰 Lancement de la roulette...")
    time.sleep(1)

    cases = list(range(8))
    resultat = random.choice(cases)

    vidéos = {
        0: "Rien",
        **{i: "Minecraft" for i in [1]},
        **{i: "Rien" for i in [2]},
        **{i: "Minecraft" for i in [3]},
        **{i: "Rien" for i in [4]},
        **{i: "Minecraft" for i in [5]},
        **{i: "Rien" for i in [6]},
        **{i: "Minecraft" for i in [7]},
    }

    nombre = vidéos[resultat]
    print(f"🎯 Résultat : {resultat} ({nombre})")

while True:
    input("\nAppuie sur Entrée pour faire tourner la roulette : ")
    lancer_roulette()