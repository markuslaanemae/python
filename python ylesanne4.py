# markus laanemäe
# 21.11.2023
# ülesanne 4







# müük

hind = 20
if hind <= 20:
    vastus = 0.1
if hind <= 10:
    vastus = 0.2
print("hinna{hind} allahindlus on {vastus} %")



"""
Ruut
Kasutaja sisestab ruudu küljed ning programm tuvastab kas tegemist saab olla ruuduga.
Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.
"""

nr1 = int(input("sisesta ruudu esimene kylg: "))
nr2 = int(input("sisesta ruudu teine kylg: "))

if nr1 == nr2:
    print("see on ruut")
else:
    print("vale asi")
    
    
"""
Matemaatika
Kasutaja sisestab kaks arvu ning programm küsib kasutajalt, mis tehet ta soovib (+-*/) ning viib kasutaja valiku ellu.
Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.
"""

nr1 = int(input("arv1: "))
nr2 = int(input("arv2: "))
tehe = input("Vali tehe + - / *:")

if tehe == "+":
    vastus = nr1 + nr2
elif tehe == "-":
    vastus = nr1 - nr2
elif tehe == "/":
        vastus = nr1 / nr2
elif tehe == "*":
    vastus = nr1 * nr2
else:
    vastus = "ära pulli mees"
    
print(f"{nr1} {tehe} {nr2} = {vastus}")
 


"""
Juubel
Kasutaja sisestab oma sünnipäeva ja sinu programm ütleb, kas tegemist on juubeliga.
Plokkskeemi pole vaja!
"""


# juubel
v = 26
if v % 5 == 0:
    Vastus = "on"
print(f"Vanus {v}: {Vastus} juubel")
