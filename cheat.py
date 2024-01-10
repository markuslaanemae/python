import math

def kuup(kylg):
    return kylg**3

def silindri(raadius, korgus):
    return math.pi*raadius**2*korgus

def kera(raadius):
    return (4/3)*math.pi*raadius**3

def kuup_print():
    print("\nKuubi ruumala arvutamiseks sisesta kuubi külje pikkus.")

def silindri_print():
    print("\nSilindri ruumala arvutamiseks sisesta silindri raadius ja kõrgus.")

def kera_print():
    print("\nKera ruumala arvutamiseks sisesta kera raadius.")

def main():
    while True:
        print("\nVali ruumala tüüp:")
        print("1. Kuup")
        print("2. Silinder")
        print("3. Kera")
        print("4. Välju")

        valik = input("Sisesta valiku number (1-4): ")

        if valik == '1':
            kuup_print()
            kylg = float(input("Sisesta kuubi külje pikkus: "))
            tulemus = kuup(kylg)
        elif valik == '2':
            silindri_print()
            raadius = float(input("Sisesta silindri raadius: "))
            korgus = float(input("Sisesta silindri kõrgus: "))
            tulemus = silindri(raadius, korgus)
        elif valik == '3':
            kera_print()
            raadius = float(input("Sisesta kera raadius: "))
            tulemus = kera(raadius)
        elif valik == '4':
            print("Programm lõpetab töö. Head aega!")
            break
        else:
            print("Vigane valik. Palun vali number vahemikus 1-4.")

        print(f"Ruumala on: {tulemus}")

        jätkamine = input("Kas soovid arvutada teise ruumala? (jah/ei): ")
        if jätkamine.lower() != 'jah':
            print("Programm lõpetab töö. Head aega!")
            break

if __name__ == "__main__":
    main()
