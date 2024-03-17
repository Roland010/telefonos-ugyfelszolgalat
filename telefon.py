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

def F2():
    global N
    with open("hivas.txt", "r") as fbe:
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

def F3():
    orak = [0] * 24
    for i in range(N):
        orak[hivasok[i].h_kezd // 3600] += 1
    for i in range(24):
        if orak[i] > 0:
            print(i, "óra", orak[i], "hívás")

def F4():
    maxhossz = 0
    maxhely = 0
    for i in range(N):
        if hivasok[i].h_vege - hivasok[i].h_kezd > maxhossz:
            maxhossz = hivasok[i].h_vege - hivasok[i].h_kezd
            maxhely = i + 1
    print("A leghosszabb ideig vonalban lévő hívó", maxhely, ". sorban szerepel,",
          "a hívás hossza:", maxhossz, "másodperc.")
