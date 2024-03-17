class Hivas:
    def __init__(self, h_kezd, h_vege):
        self.h_kezd = h_kezd
        self.h_vege = h_vege

hivasok = [None] * 1000 
N = 0 

def kiir(sz):
    print(sz)

def mpbe(ora, perc, mp):
    mp_x = ora * 3600 + perc * 60 + mp
    return mp_x

def idoszoveg(mp):
    hours = mp // 3600
    minutes = (mp % 3600) // 60
    seconds = mp % 60
    return f"{hours} {minutes} {seconds}"

def f2():
    global N
    with open("hivas.txt", "rt") as fbe:
        i = 0
        print("Adatok beolvasása...")
        for line in fbe:
            o, p, mp = map(int, line.strip().split())
            h_kezd = mpbe(o, p, mp)
            o, p, mp = map(int, fbe.readline().strip().split())
            h_vege = mpbe(o, p, mp)
            hivasok[i] = Hivas(h_kezd, h_vege)
            i += 1
        N = i - 1
        print("Beolvasott sorok száma:", N)

def f3():
    orak = [0] * 24
    for i in range(N):
        orak[hivasok[i].h_kezd // 3600] += 1
    for i in range(24):
        if orak[i] > 0:
            print(i, "óra", orak[i], "hívás")

def f4():
    maxhossz = 0
    maxhely = 0
    for i in range(N):
        if hivasok[i].h_vege - hivasok[i].h_kezd > maxhossz:
            maxhossz = hivasok[i].h_vege - hivasok[i].h_kezd
            maxhely = i + 1
    print("A leghosszabb ideig vonalban lévő hívó", maxhely, ". sorban szerepel,",
          "a hívás hossza:", maxhossz, "másodperc.")

def f5():
    ora = int(input("Kérek egy időpontot! (óra, perc, mp)\nóra: "))
    perc = int(input("perc: "))
    mp = int(input("mp: "))
    most = mpbe(ora, perc, mp)
    beszelo = 0
    varakozo = 0
    for i in range(N):
        if hivasok[i].h_kezd <= most < hivasok[i].h_vege and beszelo != 0:
            varakozo += 1
        if hivasok[i].h_kezd <= most < hivasok[i].h_vege and beszelo == 0:
            beszelo = i + 1
    if beszelo == 0:
        print("Nem volt beszélő!")
    else:
        print("Várakozók száma:", varakozo, ", a beszélő a(z)", beszelo, ". hívó.")

def f6():
    ora12 = mpbe(12, 0, 0)
    elozo = utolso = 0
    for i in range(N):
        if hivasok[i].h_kezd <= ora12 < hivasok[i].h_vege and hivasok[i].h_vege > hivasok[utolso].h_vege:
            elozo = utolso
            utolso = i
    varakozas = hivasok[elozo].h_vege - hivasok[utolso].h_kezd
    print("Az utolsó telefonáló adatai a(z)", utolso + 1, ". sorban vannak,",
          varakozas, "másodpercig várt.")

def f7():
    print("Adatok kiírása a fájlba...")
    munkakezdes = mpbe(8, 0, 0)
    ora12 = mpbe(12, 0, 0)
    vonalban = 0
    while hivasok[vonalban].h_vege < munkakezdes:
        vonalban += 1
    with open("sikeres.txt", "wt") as fki:
        if munkakezdes > hivasok[vonalban].h_kezd:
            fki.write(f"{vonalban + 1} {idoszoveg(munkakezdes)}")
        else:
            fki.write(f"{vonalban + 1} {idoszoveg(hivasok[vonalban].h_kezd)}")
        fki.write(f" {idoszoveg(hivasok[vonalban].h_vege)}\n")
        for i in range(N):
            if hivasok[i].h_kezd <= ora12 < hivasok[i].h_vege and hivasok[i].h_vege > hivasok[vonalban].h_vege:
                fki.write(f"{i + 1} {idoszoveg(max(hivasok[i].h_kezd, hivasok[vonalban].h_vege))} ")
                fki.write(f"{idoszoveg(hivasok[i].h_vege)}\n")
                vonalban = i

def main():
    kiir("2. feladat:")
    f2()
    kiir("3. feladat:")
    f3()
    kiir("4. feladat:")
    f4()
    kiir("5. feladat:")
    f5()
    kiir("6. feladat:")
    f6()
    kiir("7. feladat:")
    f7()

main()