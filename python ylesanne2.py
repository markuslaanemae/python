# markus laanemae
# 21.11.2023
# ülesanne 2
from math import *
import turtle






"""
Rulluisutaja keskmine kiirus on 29,9km/h
Kui kaugele jõuab 24minutiga
"""
kiirus = 29.9
aeg = 24
distants = round(kiirus / 60 * aeg, 2)
print("kiirusega",kiirus, "km/h jõuab",distants, "km kaugusele")





"""
Kolmnurga külgede pikkused on a=16 ja b=9
Kasuta Pythagorase teoreemi (a2 + b2 = c2) ja leia kolmnurga hüpotenuus
"""

a,b = 16,9
c = round(sqrt(a**2 + b**2),2)
print("kolmnurga hüpotenuus on" ,c)




"""
Kasutaja sisestab aja minutites
Sinu valem leiab ja väljastab tunnid ja minutid
Näiteks: sisestus 72, vastus 1:12
"""

minutid = int(input("sisesta aeg minutites: "))
h = minutid // 60
n = minutid % 60
print(h,":",n)


"""
Kasutaja sisestab täisarvu kümnendsüsteemis
Sinu programm teisendab selle 2nd ja 16nd süsteemi
"""

arv = int(input("sisesta arv: "))
bii = bin(arv)
heks = hex(arv)
print(bii, heks)


"""
Kütusekulu arvutamine
Kasutaja sisestab tangitud kütuse liitrid
Kasutaja sisestab läbitud kilomeetrid
Programm leiab kütusekulu 100km kohta keskmiselt
"""

kutus = int(input("sisesta liitrid: "))
km = int(input("sisesta läbitud dist: "))
kutuse_kulu = kutus / (km / 100)
print(kutuse_kulu)


"""
kilpkonn - küsib kasutajalt ringi raadiust
kasutab funktsiooni ringi joonistamiseks
"""



def ring(raadius):
   
    turtle.circle(raadius)

raadius = float(input("ringi loomine" "sisesta ringi raadius: "))
ring(raadius)

turtle.exitonclick()









