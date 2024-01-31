import random

def korrutamise_kontroll():
    punktid = 0

    for i in range(10):
        # Genereeri juhuslikud arvud vahemikus 1-10
        arv1 = random.randint(1, 10)
        arv2 = random.randint(1, 10)

        # Arvuta õige vastus
        oige_vastus = arv1 * arv2

        # Küsi kasutajalt vastust
        kasutaja_vastus = int(input(f"{arv1} * {arv2} = "))

        # Kontrolli vastuse õigsust
        if kasutaja_vastus == oige_vastus:
            print("Õige!")
            punktid += 1
        else:
            print("Vale! Õige vastus oli:", oige_vastus)

    print(f"Sa said kokku {punktid} punkti 10-st.")
    return punktid  # Tagasta punktid

# Käivita programm
kokku_saadud_punktid = korrutamise_kontroll()
print("Kokku saadud punktid:", kokku_saadud_punktid)
