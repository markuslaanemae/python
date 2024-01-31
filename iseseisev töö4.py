

def pronksikarva_summa(f):
    kassa = 0
    fail = open("myndid.txt")
    for mynt in fail:
        if int(mynt) <10:
            print(mynt, end="")
            kassa +=int(mynt)
    print("kassas: ", kassa)

pronksikarva_summa("mynt.txt")






# kylalised = 3
# def tervitus(n):
#     print('võõrustaja: "tere!"')
#     print(f"täna {n}. kord tervitada!")
#     print('külaline: "tere, suur tänu kutsumast!"')
# for i in range(kylalised):
#     tervitus(i+1)







# def eelarve(kylalised):
#     summa = kylalised * 10 + 55
#     return summa

# palju = int(input("Palju inimesi kutsutud: "))
# palju2 = int(input("Palju inimesi tuleb: "))
# print(f"maksimaalne eelarve: {eelarve(palju)}€")
# print(f"miinimum eelarve: {eelarve(palju2)}€")







# def mahlapakkide_arv(kg):
#     pakid = round(kg * 0.4 / 3)
#     return pakid

# kogus = float(input("Õunte kogus: "))
# print(mahlapakkide_arv(kogus))






# def banner(t):
#     print(t.upper())

# ask = int(input("mitu korda sa karjud mu peale: "))
# ask2 = input("Reklaam lause: ")


# for i in range(ask):
#     banner(ask2)



