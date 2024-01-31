# 1. Korrutamise kontrollimine
#     programm esitab korrutustehte 1p
#     ootab kasutajalt vastuse sisestamist 1p
#     kontrollib vastuse õigsust 1p
#     väljastab, kas vastus oli õige või vale. 1p
#     kokku antakse lahendamiseks 10 ülesannet. 1p

# import random

# def korrutamise_kontroll():
#     punktid = 0

#     for i in range(10):
#         arv1 = random.randint(1, 10)
#         arv2 = random.randint(1, 10)

#         oige_vastus = arv1 * arv2

#         kasutaja_vastus = int(input(f"{arv1} * {arv2} = "))

#         if kasutaja_vastus == oige_vastus:
#             print("Õige!")
#             punktid += 1
#         else:
#             print("Vale! Õige vastus oli:", oige_vastus)

#     print(f"Sa said kokku {punktid} punkti 10-st.")
#     return punktid  


# kokku_saadud_punktid = korrutamise_kontroll()
# print("Kokku saadud punktid:", kokku_saadud_punktid)




# Positiivsed ja negatiivsed
# 	tee kaks loendit positiivsete ja negatiivsete arvude hoidmiseks 1p
# 	kasutaja sisestab 5 arvu ja programm tuvastab, kumba loendisse selle lisab 2p
# 	nulli lisamisel ei tehta midagi 1p
# 	vĆ¤ljasta mĆµlemad loendit 1p

# positiivsed_arvud = []
# negatiivsed_arvud = []

# for i in range(5):
#     sisend_arv = float(input())
    
#     if sisend_arv > 0:
#         positiivsed_arvud.append(sisend_arv)
#     elif sisend_arv < 0:
#         negatiivsed_arvud.append(sisend_arv)

# print(positiivsed_arvud)
# print(negatiivsed_arvud)

# 5. Shopping List
# 	Create a program that will keep track of items for a shopping list. The program should keep asking for new items until nothing is entered (no input followed by enter/return key). The program should then display the full shopping list.

# def lisa_ostunimekiri():
#     ostunimekiri = []

#     while True:
#         ese = input("Sisesta ese ostunimekirja (vajuta Enter, et lõpetada): ")
        
#         if not ese:
#             break

#         ostunimekiri.append(ese)

#     print("\nSinu ostunimekiri:")
#     for i, ese in enumerate(ostunimekiri, start=1):
#         print(f"{i}. {ese}")


# lisa_ostunimekiri()


# 7. Eurokalkulaator - koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK vĆµi EEK->EUR.
# 	kuvatakse korrektne arusaadav kĆ¼simus ja vastus - 1p
# 	kuvatakse veateade, kui kasutaja tegi valiku valesti - 1p
# 	kĆ¼sitakse valuuta kogust ja tehakse arvutused - 2p
# 	kood kommenteeritud - 1p

# def euro_ee_kalkulaator():
    
#     valuuta_valik = input("Kas soovid arvutada EUR->EEK või EEK->EUR? (sisesta 'EUR' või 'EEK'): ")


#     if valuuta_valik.upper() not in ['EUR', 'EEK']:
#         print("Vigane sisend. Palun sisesta 'EUR' või 'EEK'.")
#         return

   
#     try:
#         kogus = float(input(f"Sisesta valuuta kogus ({valuuta_valik}): "))
#     except ValueError:
#         print("Vigane sisend. Palun sisesta numbriline väärtus.")
#         return

 
#     if valuuta_valik.upper() == 'EUR':
#         vastus = kogus * 15.6466  
#         print(f"{kogus} EUR on {vastus:.2f} EEK")
#     else:
#         vastus = kogus / 15.6466  
#         print(f"{kogus} EEK on {vastus:.2f} EUR")


# euro_ee_kalkulaator()


# 9. Emaili kontroll
# 	kasutaja lisab emaili kujul enimi.pnimi@server.com - 1p
# 	programm kontrollib kas email on sisestatud Ćµigesti - vĆ¤hemalt @-mĆ¤rgi kontroll - 1p
# 	programm tĆ¼keldab selle ja vĆ¤ljastab lause: ā€Tere enimi, sinu email on server serveris ja domeeniks on sul comā€™ - 1p
# 	kasutajalt kĆ¼situd kĆ¼simused on selgelt Ć¼heselt mĆµistetavad - 1p
# 	kood kommenteeritud - 1p

# def emaili_kontroll():
#     email = input("Sisesta oma emaili aadress: ")

#     if '@' not in email or '.' not in email:
#         print("Vigane emaili aadress. Palun sisesta korrektne email.")
#         return

#     nimi, domeen = email.split('@')
#     server, tld = domeen.split('.')

#     print(f"Tere {nimi}, sinu email on server {server} ja domeeniks on sul {tld}")

# emaili_kontroll()

# 11. Salakeel
# 	sinu programm kĆ¼sib kasutajalt, kas ta soovib salakeelt luua vĆµi tĆµlkida - 1p
# 	kasutaja sisestab tavalise sĆµna, mis muudetakse salakeeleks - 1p
# 	kasutaja sisestab salakeeles sĆµna, mis teisendatakse jĆ¤lle normaalseks - 1p
# 	kood kommenteeritud - 1p

def loo_salakeel():
    valik = input("Kas soovid luua salakeelt (sisesta 'luua') või tõlkida salakeelt (sisesta 'tõlkida'): ")

    if valik.lower() == 'luua':
        tavaline_sona = input("Sisesta tavaline sõna: ")

        salakeel = ""
        for c in tavaline_sona:
            if c.isalpha():
                salakeel += c + 'o' + c
            else:
                salakeel += c

        print("Salakeel:", salakeel)
    elif valik.lower() == 'tõlkida':
        salakeelne_sona = input("Sisesta salakeelne sõna: ")

        tavaline_sona = ""
        for i in range(0, len(salakeelne_sona), 3):
            tavaline_sona += salakeelne_sona[i]

        print("Tõlgitud sõna:", tavaline_sona)
    else:
        print("Vigane valik. Palun sisesta 'luua' või 'tõlkida'.")


loo_salakeel()



# 13. Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris vĆµi paaritu
# 	kuvatakse korrektne arusaadav kĆ¼simus ja  vastus - 1p
# 	eelnev kontroll, kas kasutaja ei lisanud arvu vĆµi pani nulli - 2p
# 	kood mis teavitab paaris vĆµi paaritust arvust - 2p
# 	kuvatakse programmi pealkiri - 1p

# def kontrolli_paaris_paaritu():
#     print("### PAARIS-PAARITU KONTROLLIJA ###")

#     sisend = input("Sisesta arv: ")

#     if not sisend:
#         print("Vigane sisend. Palun sisesta arv.")
#         return

#     try:
#         arv = int(sisend)
#     except ValueError:
#         print("Vigane sisend. Palun sisesta numbriline väärtus.")
#         return

#     if arv == 0:
#         print("Sisestatud arv on null.")
#     elif arv % 2 == 0:
#         print(f"{arv} on paaris arv.")
#     else:
#         print(f"{arv} on paaritu arv.")

# kontrolli_paaris_paaritu()

# 15. Temperatuurid - Programm peab tĆ¶Ć¶tlema Ć¼he aasta kĆµigi pĆ¤evade temperatuure. Kirjutada programm, mis leiab kuude kaupa, mitmendal kuupĆ¤eval oli kĆµige soojem. VĆ¤ljasta kuupĆ¤ev ja vastav temperatuur. (Kui sama temperatuuriga oli mitu pĆ¤eva, vĆ¤ljasta vĆ¤hemalt Ć¼ks)

# 	jaanuar -16 -12 -15 -20 0 -1 -20 -2 -20 -14 -18 -8 2 -1 -14 -7 -15 -17 -6 -17 -17 -7 0 3 -20 -17 -15 -8 -12 3
# 	veebruar -9 -2 -7 1 -16 -19 -19 -11 -16 -15 -9 -2 -16 -4 -20 -5 -6 -17 -5 0 -16 2 0 -20 -16 -2 -18
# 	mĆ¤rts 2 -9 -1 -3 -6 -2 1 -2 -3 -9 -1 -4 0 -6 -7 1 0 2 -5 -10 2 -7 -3 2 -10 2 -9 -8 -5 -2
# 	aprill -5 0 10 -9 0 -9 -8 6 -5 3 -1 4 9 -1 2 0 10 0 5 0 -10 0 6 3 -6 -2 -10 -8 -2
# 	mai 12 5 8 -1 -2 4 10 -1 7 15 7 3 6 4 10 9 13 6 14 10 14 2 6 12 15 2 14 11 9 1
# 	juuni 12 5 17 6 10 14 9 7 15 23 29 11 16 18 9 25 14 8 16 22 19 22 23 18 16 16 26 24 22
# 	juuli 15 8 21 28 18 13 9 9 8 6 8 12 12 29 28 20 6 9 12 8 14 18 14 13 23 6 24 24 17 20
# 	august 7 6 5 19 18 18 17 20 15 11 7 10 13 12 20 11 10 14 18 14 24 6 17 16 6 17 5 13 11
# 	september 21 19 21 9 13 18 6 6 20 7 25 13 8 9 14 16 19 10 7 25 7 17 16 15 17 18 15 9 19
# 	oktoober 2 2 1 5 -2 5 5 2 2 2 1 -2 1 -2 0 -2 5 4 0 1 -1 2 0 2 2 2 -1 1 4 -1
# 	november -6 -7 -2 -7 -2 -4 0 -7 -8 -6 0 -9 -2 -3 -2 0 -8 -2 -5 -2 -5 -8 -10 0 -2 -9 -9 -7 -1
# 	detsember -15 2 -11 -14 -15 -5 -5 -18 -18 -19 0 0 2 -7 -16 -7 -4 -1 -1 -16 -18 -10 -3 -19 -6 -16 -16 -8 -2 -18

# temperatuurid = {
#     "jaanuar": [-16, -12, -15, -20, 0, -1, -20, -2, -20, -14, -18, -8, 2, -1, -14, -7, -15, -17, -6, -17, -17, -7, 0, 3, -20, -17, -15, -8, -12, 3],
#     "veebruar": [-9, -2, -7, 1, -16, -19, -19, -11, -16, -15, -9, -2, -16, -4, -20, -5, -6, -17, -5, 0, -16, 2, 0, -20, -16, -2, -18],
#     "märts": [2, -9, -1, -3, -6, -2, 1, -2, -3, -9, -1, -4, 0, -6, -7, 1, 0, 2, -5, -10, 2, -7, -3, 2, -10, 2, -9, -8, -5, -2],
#     "aprill": [-5, 0, 10, -9, 0, -9, -8, 6, -5, 3, -1, 4, 9, -1, 2, 0, 10, 0, 5, 0, -10, 0, 6, 3, -6, -2, -10, -8, -2],
#     "mai": [12, 5, 8, -1, -2, 4, 10, -1, 7, 15, 7, 3, 6, 4, 10, 9, 13, 6, 14, 10, 14, 2, 6, 12, 15, 2, 14, 11, 9, 1],
#     "juuni": [12, 5, 17, 6, 10, 14, 9, 7, 15, 23, 29, 11, 16, 18, 9, 25, 14, 8, 16, 22, 19, 22, 23, 18, 16, 16, 26, 24, 22],
#     "juuli": [15, 8, 21, 28, 18, 13, 9, 9, 8, 6, 8, 12, 12, 29, 28, 20, 6, 9, 12, 8, 14, 18, 14, 13, 23, 6, 24, 24, 17, 20],
#     "august": [7, 6, 5, 19, 18, 18, 17, 20, 15, 11, 7, 10, 13, 12, 20, 11, 10, 14, 18, 14, 24, 6, 17, 16, 6, 17, 5, 13, 11],
#     "september": [21, 19, 21, 9, 13, 18, 6, 6, 20, 7, 25, 13, 8, 9, 14, 16, 19, 10, 7, 25, 7, 17, 16, 15, 17, 18, 15, 9, 19],
#     "oktoober": [2, 2, 1, 5, -2, 5, 5, 2, 2, 2, 1, -2, 1, -2, 0, -2, 5, 4, 0, 1, -1, 2, 0, 2, 2, 2, -1, 1, 4, -1],
#     "november": [-6, -7, -2, -7, -2, -4, 0, -7, -8, -6, 0, -9, -2, -3, -2, 0, -8, -2, -5, -2, -5, -8, -10, 0, -2, -9, -9, -7, -1],
#     "detsember": [-15, 2, -11, -14, -15, -5, -5, -18, -18, -19, 0, 0, 2, -7, -16, -7, -4, -1, -1, -16, -18, -10, -3, -19, -6, -16, -16, -8, -2, -18]
# }

# kuu_nimed = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]

# def leia_soem_kuupaev():
#     max_temp = float('-inf')
#     soojem_kuupaev = ""
    
#     for kuu, temperatuurid_kuus in enumerate(temperatuurid.values(), start=1):
#         max_temp_kuus = max(temperatuurid_kuus)
#         if max_temp_kuus > max_temp:
#             max_temp = max_temp_kuus
#             soojem_kuupaev = f"{kuu_nimed[kuu-1]} {temperatuurid_kuus.index(max_temp_kuus) + 1}"

#     print(f"Kõige soojem kuupäev oli {soojem_kuupaev} temperatuuriga {max_temp} kraadi.")

# leia_soem_kuupaev()


# 17. Email
# 	Kasutaja lisab emaili kujul enimi.pnimi@server.com
# 	Programm kontrollib kas email on sisestatud Ćµigesti
# 	Programm tĆ¼keldab selle ja vĆ¤ljastab lause: Tere enimi, sinu email on server serveris ja domeeniks on sul com


# def kontrolli_email():
   
#     email = input("Sisesta oma emaili aadress: ")

#     if '@' not in email or '.' not in email:
#         print("Vigane emaili aadress. Palun sisesta korrektne email.")
#         return

#     nimi, domeen = email.split('@')
#     server, tld = domeen.split('.')

#     print(f"Tere {nimi}, sinu email on server {server} ja domeeniks on sul {tld}")

# kontrolli_email()
