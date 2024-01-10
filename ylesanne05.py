#massiivid - array
#28.11.23
#m.laanemae

"""
Loo vanuste loend. Leia numbrite suurim ja väikseim arv, kogusumma, keskmine
Kasuta loendis olevate arvude väärtusi ning loo tärnide abil lintdiagramm.
"""

from audioop import avg


vanused = [123,2,31,4,77,34,65,17]
print(f"suurim arv {max(vanused)} ja väiksem arv {min(vanused)}")
print(f"vanuste summa: {sum(vanused)}")
print(f"vanuse kesmine: {sum(vanused)/len(vanused)}")
for vanus in vanused:
    print(vanus*"*")








"""
Tekita loend, kuhu oled lisanud meelega mõned ühesugused nimed.
Loo kood, mis ei väljasta kordusi.
"""
"""
opilased = ['Juhan','Kati','Mario','Mario','Mati','Mati']
uus_opilased = []
for opilane in opilased:
    if opilane not in uus_opilased:
        uus_opilased.append(opilane)

print(uus_opilased)






print("")
input()

"""
"""
Õpilased
Loo õpilaste nimedest loend. Programm lubab loendis olevaid nimesid muuta.
"""
"""
opilased = ['Juhan','Kati','Maarja','Mario','Mati']
jrk = 1
for opilane in opilased:
    print(f"{jrk}. {opilane}")
    jrk+=1
valik = int(input("mitmendat nime tahad muuta: "))
uusnimi = input("lisa uus nimi: ")
del opilased[valik-1]
opilased.insert(valik-1, uusnimi)



print(opilased)

"""
"""

Nimede lisamine loendisse
Küsi kasutajalt viis nime. Salvesta need loendisse ja kuva tähestikulises järjekorras. Kuva eraldi viimati lisatud nimi.



nimed = []

for i in range(5):
    nimi = input("lisa nimi: ")
    nimed.append(nimi)
print("viimati lisatud nimed:",nimed)
nimed.sort()


print (nimed)
"""




