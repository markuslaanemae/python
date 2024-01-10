"""
1.Sinu ülesanne on koostada programm, mis kuvab pooliitikud inimsilmale sõbralikus vaates. https://metshein.com/python/s6pru_l6ustaraamatus.txt 
Andra      Veidemann  SDE        3469      
Evelyn     Sepp       KE         3569      
Juku-Kalle Raid       IRL        4275      
Jörgen     Siil       SDE        1865      
Keit       Pentus     RE         3026      
Kristiina  Ojuland    RE         4067      
Liisa      Pakosta    IRL        2455      
Margus     Tsahkna    IRL        2534      
Marko      Mihkelson  RE         1504      
Mart       Laar       IRL        2711  


2.Täienda eelmist programmi nii, et kuvataks kui palju on nimekirjas kodanikke Reformierakonnast ja kui palju Keskerakonnast
    Reformikaid: 3
    Kesikuid: 1
3.Täienda programmi veelgi ja leia, kui palju oli erinevaid erakondi kokku.
    Erakondi kokku: 4
4,Viimase täiendusena salvestab sinu programm ainult poliitikute nimed uude faili (loetavalt).
 """




 #faili avamine
fail = open("l6ustaraamat.txt", "r")
erakonnad = []
re = 0
ke = 0
#faili sisu kuvamine
for rida in fail:
    #enimi, perenimi, erak, sobrad = rida.split(" ")
    poliitik = rida.split(" ")
    print(f"{poliitik[0]:10} {poliitik[1]:10} {poliitik[2]:4} {poliitik[3]}", end="")
    if poliitik[2]=="RE":
        re+=1
    elif poliitik[2]=="KE":
        ke+=1
    if poliitik[2] not in erakonnad:
        erakonnad.append(poliitik[2])
    with open("pollitikud.txt","a") as kirjutamiseks:
        kirjutamiseks.write(poliitik[0]+" "+poliitik[1]+"\n")

print()
print(f"reformikad: {re} \nkesikud: {ke}")
print(f"erakondi kokku: {len(erakonnad)}")
fail.close


