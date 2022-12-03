"""1. feladat"""
import random
import math

tomb = [int((random.random()*8))+5, 5, 11, -2, 4]


def elsofeladat(szeparator=" "):

    i = 0
    szoveg = ""
    while i < len(tomb):
        if i < len(tomb)-1:
            szoveg += str(tomb[i]) + szeparator
        elif i == len(tomb)-1:
            szoveg += (str(tomb[i]))
        i+=1
    print(szoveg)


def beker():

    szam = 0
    while ((szam < 10 or szam > 100) or (szam % 3 != 0 or szam % 2 == 0)):
        szam = int(input("Kérek egy 3-mal osztható páratlan kétjegyű számot: "))
    tomb.append(szam)


beker()
elsofeladat("#")
elsofeladat(".")
elsofeladat()

def prim_e():

    i = 0
    j = 2
    szamlalo = 0
    while i < len(tomb):
        while j < tomb[i]:
            if tomb[i] % j != 0:
                szamlalo += 1
            j += 1
        i += 1
    print(f"{szamlalo} prímszám van a listában.")

prim_e()