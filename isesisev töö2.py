#markus laanemäe
#18.12.2023
#iseseisevtöö


import random
import winsound




def aratus(nr):
    for i in range(nr):
        winsound.Beep(2500, 250)
        print("tõuse ja sära!")

#jänku

def porgandid(r):
    joostud_ringid = 0
    porgandid = 0
    while joostud_ringid < r:
        joostud_ringid+=1
        if joostud_ringid%2==0:
            porgandid+=joostud_ringid





    print(f"jänkulaps saab: {porgandid} porgandit" )






def taringud(arv):
    for i in range(arv):
        print(random.randint(1,6))

        
def male(arv):
    nisuterad = 1
    ruut = 1
    while ruut < arv:
        ruut+=1
        nisuterad = nisuterad*2
        
        

    print(nisuterad)




def lumivalgeke(p):
    ounad = 14
    for i in range(p):
        oun=random.randint(1,2)
        ounad-=oun
        print(oun)
    print(f"lumivalgekesele jäi {ounad} õuna")








lumivalgeke(6)

# male(24)

#taringud(2)

# kordused = int(input("äratuste arv: "))
# aratus(kordused)

# ringid = int(input("mitu ringi jooksis: "))
# porgandid(ringid)