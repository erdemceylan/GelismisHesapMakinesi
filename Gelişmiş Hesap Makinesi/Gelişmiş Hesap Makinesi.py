import math
import time
def Topla(sayi1,sayi2):
    print("{}+{} =".format(sayi1,sayi2),sayi1+sayi2)
def Cikar(sayi1,sayi2):
    print("{}-{} =".format(sayi1,sayi2),sayi1-sayi2)
def Carp(sayi1,sayi2):
    print("{}*{} =".format(sayi1,sayi2),sayi1*sayi2)
def Bol(sayi1,sayi2):
    print("{}/{} =".format(sayi1,sayi2),sayi1/sayi2)
def Faktoriyel(sayi):
    faktoriyel=math.factorial(sayi)
    print("{}! =".format(sayi),faktoriyel)
def KalanBul(sayi1,sayi2):
    kalan=math.fmod(sayi1,sayi2)
    print("{} Sayısının {} Sayısına Bölümünden Kalanı =".format(sayi1,sayi2),kalan)
def Ebob(sayi1,sayi2):
    cevap=math.gcd(sayi1,sayi2)
    print("{} ile {} Sayılarının EBOB'u =".format(sayi1,sayi2),cevap)
def Kuvvet(sayi1,sayi2):
    cevap=math.pow(sayi1,sayi2)
    print("{} Sayısının {}.Dereceden Kuvveti =".format(sayi1,sayi2),cevap)
def Karakok(sayi):
    cevap=math.sqrt(sayi)
    print("{} Sayısının Karakökü=".format(sayi),cevap)
def Sinus(sayi):
    cevap=math.sin(sayi)
    print("{}'in Sinüsü =".format(sayi),cevap)
def Cosinus(sayi):
    cevap=math.cos(sayi)
    print("{}'in Cosinüsü =".format(sayi),cevap)
print("""
********************************
        HESAP MAKİNESİ
********************************

0-Çıkış
1-Toplama
2-Çıkarma
3-Çarpma
4-Bölme
5-Faktöriyel Alma
6-Kalan Bulma
7-EBOB Hesaplama
8-Kuvvet Alma
9-Karakök Hesaplama
10-Sinüs Hesaplama
11-Cosinüs Hesaplama

""")
while True:
    secim = int(input("Yapmak İstediğiniz İşlem:"))
    if (secim == 1):
        sayi1 = int(input("1.Sayı:"))
        sayi2 = int(input("2.Sayı:"))
        print("İşlem Yapılıyor. Lütfen Bekleyiniz.")
        time.sleep(1)
        Topla(sayi1, sayi2)
    elif (secim == 2):
        sayi1 = int(input("1.Sayı:"))
        sayi2 = int(input("2.Sayı:"))
        print("İşlem Yapılıyor. Lütfen Bekleyiniz.")
        time.sleep(1)
        Cikar(sayi1, sayi2)
    elif (secim == 3):
        sayi1 = int(input("1.Sayı:"))
        sayi2 = int(input("2.Sayı:"))
        print("İşlem Yapılıyor. Lütfen Bekleyiniz.")
        time.sleep(1)
        Carp(sayi1, sayi2)
    elif (secim == 4):
        sayi1 = int(input("1.Sayı:"))
        sayi2 = int(input("2.Sayı:"))
        print("İşlem Yapılıyor. Lütfen Bekleyiniz.")
        time.sleep(1)
        Bol(sayi1, sayi2)
    elif (secim == 5):
        sayi = int(input("Sayı:"))
        print("İşlem Yapılıyor. Lütfen Bekleyiniz.")
        time.sleep(1)
        Faktoriyel(sayi)
    elif (secim == 6):
        sayi1 = int(input("1.Sayı:"))
        sayi2 = int(input("2.Sayı:"))
        print("İşlem Yapılıyor. Lütfen Bekleyiniz.")
        time.sleep(1)
        KalanBul(sayi1, sayi2)
    elif (secim == 7):
        sayi1 = int(input("1.Sayı:"))
        sayi2 = int(input("2.Sayı:"))
        print("İşlem Yapılıyor. Lütfen Bekleyiniz.")
        time.sleep(1)
        Ebob(sayi1, sayi2)
    elif (secim == 8):
        sayi = int(input("Sayı:"))
        kuvvet = int(input("Kuvvet"))
        print("İşlem Yapılıyor. Lütfen Bekleyiniz.")
        time.sleep(1)
        Kuvvet(sayi, kuvvet)
    elif (secim == 9):
        sayi = int(input("Sayı:"))
        print("İşlem Yapılıyor. Lütfen Bekleyiniz.")
        time.sleep(1)
        Karakok(sayi)
    elif (secim == 10):
        sayi = int(input("Sayı:"))
        print("İşlem Yapılıyor. Lütfen Bekleyiniz.")
        time.sleep(1)
        Sinus(sayi)
    elif (secim == 11):
        sayi = int(input("Sayı:"))
        print("İşlem Yapılıyor. Lütfen Bekleyiniz.")
        time.sleep(1)
        Cosinus(sayi)
    elif (secim == 0):
        print("Çıkış Yapılıyor. Lütfen Bekleyiniz.")
        time.sleep(2)
        print("Çıkış Yapıldı. İyi Günler.")
        break