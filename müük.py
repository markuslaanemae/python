# müük
import random

hind = 25
if hind <= 10:
    vastus = 0.1
else:
    vastus = 0.2
print(f"allahindlus on: ",hind - (hind * vastus))



"""
Sa pead looma programmi, mis kontrollib kas kandideerija sobib antud meeskonda.
Vanus peab jääma vahemikku 16-18 ning lubatud on ainult meessugu.
Täienda programmi nii, et kui kandideerija on naissoost, siis vanust üldse ei küsita.
"""

sugu = "naine"
if sugu == "mees":
    vanus = 28
    if vanus >= 16 and vanus <= 18:
        print("Tere tulemast meeskonda")
    else:
        print("vanus ei sobi")
else:
    print("ei pääse meeskonda")


"""
Tärnid
Loo tsükkel, mis väljastab 5×5 tärnid
Loo tsükkel, mis väljastab tärnidest kasvava kolmnurga
Loo tsükkel, mis väljastab tärnidest kahaneva kolmnurga
"""
j = 5
for i in range(5):
    print("* "*j)
    j = j - 1
for i in range(j):
    print("* "*(i+1))
    

"""
Loto
Koosta tsükli abil programm, mis kuvab 5 suvalist  ühekohalist numbrit. Näiteks 53542
"""

for x in range(5):
    print(random.randint(0,9),end="")

print()



"""
Loo tsükkel, mis genereerib arvud 1-100 koos vastava tekstiga, kas arv on paaris või paaritu
"""

for p in range(1,11):
    if p % 2 == 0:
        v = "Paaris"
    else:
        v = "paaritu"
    print(p,v)