#markus laanemäe
#18.12.2023
#iseseisevtöö

import random



#rebased
# fail = open("rebased.txt", encoding="utf-8")
# vastuvoetud = []
# for rida in fail:
#     vastuvoetud.append(int(rida))
    
# fail.close()


#sissetulekud
# fail = open("konto.txt")
# for i in fail:
#     if float(i) > 0:
#         print(i,end="")



#jukebox
# siiamidagi = input("Anna failinimi: ")
# fail = open(siiamidagi, encoding ="utf-8")
# print("Muusikapalade valik")
# nr = 1
# for i in fail:
#     print(f"{nr}. {i}",end="")
#     nr+=1
# valik = int(input("\n Vali laulu number: "))
# fail.seek(0)
# nr = 1
# for i in fail:
#     if nr == valik:
#         print(i)
#     nr+=1


import datetime
paev = datetime.datetime.now().day

#tahvli juurde
fail = open("nimekiri.txt", encoding="utf-8")
nr = 1
for nimi in fail:
    if nr == paev:
        print(nimi, end="")
    nr+=1