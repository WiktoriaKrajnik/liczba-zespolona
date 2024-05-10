import math


class liczbazespolona:
    def __init__(self, re, im):
        self.re = re
        self.im = im
        print("Liczba zespolona: " + str(self.re) +"+"+ str(self.im) + "i")
        
    def moduł(self):
        z = math.sqrt(math.pow(self.re, 2) + math.pow(self.im, 2))
        print("Moduł z liczby zespolonej to: " + str(z))
    
    @staticmethod
    def dodaj(liczba1, liczba2):
        a = liczba1.re + liczba2.re
        b = liczba1.im + liczba2.im
        print(str(a) + "+" + str(b) + "i")
    
    @staticmethod
    def mnozenie(liczba1, liczba2):
        a = liczba1.re * liczba2.re
        b = liczba1.re * liczba2.im + liczba1.im * liczba2.re
        c = liczba1.im * liczba2.im
        print(str(a)+ "+" + str(b) + "i" + "+" + str(c) + "i^2")


poczatek ="L"
lista_liczb =[]
i = 1
która = int(input("ile liczb chcesz wpisać: "))
while(i<=która):
    print("Wpisz informacje o liczbie")
    re = int(input("a jest równe: "))
    im = int(input("b jest równe: "))
    Liczba = poczatek + str(i)
    Liczba = liczbazespolona(re, im)
    Liczba.moduł()
    lista_liczb.append(Liczba)
    i+=1
odp = input("Czy chcesz dodać lub pomnożyc dwie liczby zespolone? ")
if odp.capitalize() == "Tak":
    odp = input("Chcesz dodać czy pomnożyć? ")
    if odp.capitalize() == "Dodać":
        Liczba1 = int(input("Jaką pierwszą liczbę chcesz dodać(numer): "))
        Liczba2 = int(input("Jaką druga liczbę chcesz dodać(numer): "))
        p = lista_liczb[Liczba1 - 1]
        d = lista_liczb[Liczba2 - 1]
        liczbazespolona.dodaj( p, d)
    
    elif odp.capitalize() == "Pomnożyć":
        Liczba1 = int(input("Jaką pierwszą liczbę chcesz pomnożyć(numer): "))
        Liczba2 = int(input("Jaką druga liczbę chcesz pomnożyć(numer): "))
        p = lista_liczb[Liczba1 - 1]
        d = lista_liczb[Liczba2 - 1]
        liczbazespolona.mnozenie( p, d)
    else:
        print("Nie ma takiego działania")    



        