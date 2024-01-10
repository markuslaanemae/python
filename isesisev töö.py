#markus laanemäe
#18.12.2023
#iseseisevtöö


# ●	Koostada programm, mis väljastaks ekraanile teksti Tere, maailm! täpselt sellisel kujul - koma ja hüüumärgiga

def tere():
    print(f"Tere, maailm!")



# ●	1. real luuakse muutuja nimega aasta ning antakse sellele väärtuseks 2020 (arvuna);
# ●	2. real luuakse muutuja nimega liblikas ning antakse sellele väärtuseks "teelehe-mosaiikliblikas" (sõnena);
# ●	3. real luuakse muutuja nimega lause_keskosa ning antakse sellele väärtuseks ". aasta liblikas on " (sõnena);
# ●	4. real luuakse muutuja nimega lause, mille väärtuse saamiseks ühendatakse üheks sõnaks muutujad aasta, lause_keskosa ja liblikas (vajadusel tuleb kasutada funktsiooni, mis teisendab arvu sõneks);
# ●	5. real väljastatakse muutuja lause väärtus ekraanile.


def aasta_liblikas():
    aasta = 2020
    liblikas = "teelehemosaiikliblikas"
    lause_keskosa = ". aasta liblikas on "
    lause =str(aasta)+lause_keskosa+liblikas
    print(lause)


# ●	küsib kasutajalt pilvede aluse kõrgust (kilomeetrites),
# ●	väljastab ekraanile Need on ülemised pilved, kui sisestatu on üle 6,0 km,
# ●	väljastab Need ei ole ülemised pilved, kui kõrgus on 6,0 km või alla selle.

def pilved(alus):
    if alus > 6:
        print("need on ülemised pilved")
    else:
       print("need ei ole ülemised pilved")




def bussideArv(i, k):
    bussid = i % k
    if i == k:
        bussid = i // k
        Viimases = i
    elif bussid > 0:
        bussid = i // k +1
        Viimases = i % k
    else:
        bussid = i // k
        Viimases = k
    print(f"busse vaja:{bussid}. \nViimases bussis: {Viimases} inimest")






tere()
aasta_liblikas()
alus = float(input("pilvede aluse kõrgus (kilomeetrites):"))
pilved(alus)
inimesed = int(input("inimeste arv:"))
kohti_bussis = int(input("kohtade arv bussis:"))
bussideArv(inimesed, kohti_bussis)
