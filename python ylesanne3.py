# markus laanemäe
# 21.11.2023
# ülesanne 3

"""
Palindroom
Mis on palindroom?
Sinu programm peab kontrollima, kas minu sisestatud tekst on palindroom või mitte.
"""



def is_palindrome(text):
    
    cleaned_text = ''.join(text.lower().split())

    
    return cleaned_text == cleaned_text[::-1]


user_input = input("Sisesta tekst: ")


if is_palindrome(user_input):
    print("Sisestatud tekst on palindroom.")
else:
    print("Sisestatud tekst ei ole palindroom.")







"""
Tundide ajad
Kasutaja sisestab tundide alguse ja lõpu. Näiteks 8:30 ja 14:15
Sinu programm leiab, kui pikk oli õpilase päev
Väljasta täislause ja kasuta vormindamisel format() meetodit.
"""

algus = input("tundide algus: ")
lopp = input("tundide lõpp: ")

hh1,mm1 = algus.split(":")
hh2,mm2 = lopp.split(":")

algus_minutid = int(hh1) * 60 + int(mm1)
lopu_minutid = int(hh2) * 60 + int(mm2)

ajavahe = lopu_minutid - algus_minutid
tunnid = ajavahe // 60
minutid = ajavahe % 60

print(f"{tunnid}:{minutid}")



"""
Korralik nimi
Küsi kasutajalt nime
Tervita teda ja sinu programm väljastab nime kirjapildi õigesti – suure algustähega ja eemaldab ülearused tühikud
Näiteks: sisend–>mARiO; väljund–>Tere, Mario!
"""


ask = input("Sisesta nimi: ")

print(f"Tere, {ask.strip().capitalize()}")



"""
Vandumine
Kui kasutaja sisestab “kogemata” teksti, kus leidub sõna ‘kurat’, siis sinu programm asendab need tärnidega.
Näiteks: sisend–>Kurat küll!; väljund–>*** küll!
"""

ask = input("Sisesta tekst: ")

print(f"{ask.replace('kurat','****')}")


"""
Email
Küsi kasutajalt emaili ja kontrolli, kas see sisaldas @-märki.
Näiteks: sisend–>minu@mail.ee; väljund–> True või False
"""

ask = input("Sisesta email: ")

print('@' in ask)

