#Introduction to Number and String
9 #int
9.2 #float

print('Azmi Can Konur') # write on console
"Azmi Can Konur" 

type(9.2) #type
 
123
type(123)
"123"
type("123")

# STRING METODLARI 

a=9
b=8

"a" + "b"
"a"  "b"
"a" - "b" # !
"a"*3
"a "*3

gel_yaz = "gelecegi_yazanlar"

#del gel_yaz #sisteme giren isim değişkenini silmek için del

len(gel_yaz) #boyut 
gel_yaz.upper() #büyük harflere çevirme 
gel_yaz.lower()() #küçük harflere çevirme

gel_yaz.islower() #string küçük harf mi ? islower()
B = gel_yaz.upper()
B.isupper() #string büyük harf mi ? kontrol

gel_yaz.replace("e","a") #harfleri değiştirme
ad_soyad = "*Azmi Can Konur*"
ad_soyad.strip("*")

gel_yaz = "gelecegi_yazanlar"
dir(ad_soyad) #kullanabilcek methodlar

#SUBSTRINGLER
gel_yaz = "gelecegi_yazanlar"
gel_yaz[1]
gel_yaz[0:3] # e kadar 'gel'


#DEGISKENLER

a = 9
b = "ali_uzaya_git"
c = a*6

#TYPE_DONUSUMLERI

toplama_bir = input()
toplama_iki = input()

type(toplama_bir)

toplam = int(toplama_bir)+ int(toplama_iki)

#int()
#float()
#str()

#print()

print("Azmi Can")

print("Azmi","Can", sep = "_")

print()
?print #print komutunun kullanım alanları
 
#Veri Yapıları

#Listeler #sıralı

#[]
#list()

notlar = [80,70,50,60]
type(notlar)


liste1 = ["a",19.3,90,notlar]

len(liste)

type(liste[0])

tum_liste = [liste, notlar]

# del tum_liste

#Listeler-Eleman  Islemleri

liste = [10,20,30,40,50]
liste.pop(1)
liste.extend(liste)
liste[1]
liste[:2] # sıfrdan 2 ye kadar

yeni_liste = ["a",10,[20,30,50]]


yeni_liste[2][1]

#del liste

#insert

liste = ["ali","veli","isik"]

liste.insert(0, "azmi")
liste

liste.insert(len(liste),"konur")
liste

#pop

liste.pop(0)
liste

#count aynı index kaç tane var ?

liste = ["ali","veli","isik","ali","veli"]

liste.count("ali")

#copy ilk halini saklamak

liste_yedek = liste.copy()

#extend iki listeyi birleştirme

liste.extend(["a",10,5])
liste

#index bir elemanın hangi indekste oldugunu

liste.index("veli")

#reverse elemanları terse çevirme

liste.reverse()
liste

#sort() sıralama

liste = [10,5,78,12]

liste.sort()
liste

#clear

liste.clear()

#Tuple-Veri Yapıları DEGISTIRILEMEZ sıralı kapsayıcı

#tuple oluşturma 

t = ("ali","veli",1,2,2.3,[1,2,3,4])

t = "ali","veli",1,2,2.3,[1,2,3,4]

#tuple()

t = ("eleman",)
type(t)

#Tuple Eleman Islmeleri

t = ("ali","veli",1,2,2.3,[1,2,3,4])
t
t[1]
t[0:3]

t[2] = 99 #degistirelmez hatası alır 

# Veri Yapıları - Dictionary (SÖZLÜK)
#Kapsayıcıdır-Sırazsızdır-Değişterilirdir referanslı yapı

sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART" :"Classification and Reg"}

sozluk

len(sozluk)


sozluk = {"REG" : 10,
          "LOJ" : 20,
          "CART" :30}

sozluk


sozluk = {"REG" : ["RMSE",10],
          "LOJ" : ["MSE",20],
          "CART" :["SE",30]}

sozluk

#Sozluk Eleman ISlemleri

sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART" :"Classification and Reg"}

sozluk[0] #hata alıyoruz Nedeni sırasız olması
sozluk["REG"]
sozluk["LOJ"]

sozluk = {"REG" : ["RMSE",10],
          "LOJ" : ["MSE",20],
          "CART" :["SE",30]}
sozluk["REG"]

sozluk = {"REG" : {"RMSE" : 10,
                   "MSE"  : 20,
                   "SSE"  : 30},
          "LOJ" :  {"RMSE" : 10,
                   "MSE"  : 20,
                   "SSE"  : 30},
          "CART" : {"RMSE" : 10,
                   "MSE"  : 20,
                   "SSE"  : 30}}
sozluk
sozluk["REG"]["SSE"]

#Sozluk - Eleman Eklemek& Degistirmek

sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART" :"Classification and Reg"}

sozluk["GBM"] = "Gradient Boosting Mac"
sozluk

sozluk["REG"] = "Coklu Dogrusal Regrasyon"
sozluk

sozluk[1] = "Yapay sinir agları"
sozluk

l = [1]
l

sozluk[l]="yeni" #hata verdi  key sabit veri yapıları kullanılır

t = ("tuple",)

sozluk[t] = "yeni"
sozluk

#Veri Yapilari-Setler
#SIRaSIZDIR ,Degistirebilr,Farklı tip barındırabilir,DEgerleri essizdir Tektir.

#SET olsuturmak

s = set()
s

l = [1,"a","ali",123]
s = set(l)
s

t =  ("a","ali")
s = set(t)
s

ali = "lutfen_ata_bak ma_uzaya_git"
type(ali)

s = set(ali)
s

l = ["ali","lütfen","ata","bakma","uzaya","git","git","ali","git"]
l

s = set(l)
s

len(s)

l[0]

s[0] #setler sırasız!!

# eleman ekleme cıkarma

l = ["gelecegi","yazanlar"]
s = set(l)
s
dir(s)

s.add("ile")
s

s.add("gelecege_git")
s

s.add("ile") #var oldugu için eklemiyor
s

s.remove("ali") #icindeki elamanı silme yoksa hata 
s
 
s.discard("ali") #icinde yoksa bile hata vermez
s

#Setler - Klasik Kume Islemleri

#differance() ile kumenin farkını ya da "-"

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.difference(set2) # olmayan deger


set2.difference(set1)

set1.symmetric_difference(set2) # iksinde de olmayan

set1 - set2
set2 - set1


# intersection() & union

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.intersection(set2) # ortak kesisim

kesisim = set1 & set2 # ortak

bırlesim = set1.union(set2) # birlesme
bırlesim

#Set Sorgu Islmeleri

set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])

#iki kumenin kesisiminin bo olup olmadıgını sorgulama

set1.isdisjoint(set2) #bos mu? 

#bir kümenin butun elemanlarının baska bir  kume icerisdne yer alıp  almadigi


set1.issubset(set2) #set1 set2 nin alt kümesi mi ?

#bir kümenin bir diger kumeyi kapsayıp kapsamadiği

set2.issuperset(set1)

# FONKSIYONLARA GIRIS VE FONKSIYON OKUR YAZARLIK

# Fonksiyon Yazma

def kare_al(x):
    print(x**2)

kare_al(3)

# Bilgi Notuyla Çıktı Uretmek

def kare_al(x):
    print(x**2)

kare_al(3)

def kare_al(x):
    print("girilen sayının karesi:"+ str(x**2))

kare_al(5)

def kare_al(x):
    print("girilen sayı:" + str(x) + " karesi:"+ str(x**2))

#IKI Argumanlı Fonksiyon Tanımlamak

def kare_al(x):
    print(x**2)


def carpma_yap(x,y):
    print(x*y)    

carpma_yap(2, 3)

# ON TANIMLI Argumanlar

def carpma_yap(x,y=1):
    print(x*y)

carpma_yap(3)                

#Argumanlarin Siralamasi

def carpma_yap(x,y=1):
    print(x*y)

carpma_yap(y=2, x=3)

carpma_yap(2,3)

# Ciktiyi Girdi Olarak Kullanmak

def direk_hesap(isi,nem,sarj):
    print((isi+nem)/sarj)

cikti = direk_hesap(25, 40, 70)
cikti                           # hata
print(cikti)                    #hata
direk_hesap(25, 40, 70)*9       #hata

def direk_hesap(isi,nem,sarj):
    return (isi+nem)/sarj  #burda durur alttakilerin bir önemi olmaz

cikti = direk_hesap(25, 40, 70)
cikti
direk_hesap(25, 40, 70)*9

# Local ve Global Degiskenler

x=10 #Global
y=20

def carpma_yap(x=2,y=1): #gecici degiskenler
    return x*y

carpma_yap(2, 3)

#Local Etki Alanlaindan Global Etki Alanini DEgistirme

x = []

def add_index(y):
    x.append(y)
    print(str(y) + " ifadesi eklendi")
    
add_index("ali")

add_index("veli")

x

# KARAR & KONTROL YAPILARI

#True-False Sorgulamaları

sinir = 5000
sinir == 4000 

5 == 5


#if

sinir = 50000
gelir = 60000

if gelir < sinir:
    print("gelir sinridan kücük")
   
if sinir < gelir:
    print("gelir sinridan büyük")
else:
    print("gelir sinirdan küçük")

# else

sinir = 50000
gelir = 20000
 


if sinir < gelir:
    print("gelir sinridan büyük")
else:
    print("gelir sinirdan küçük")
    
# Uygulama
sinir = 50000
magaza_adi = input("Mağaza Adi Nedir?")
gelir = int(input("Gelirinizi Giriniz: "))

if gelir > sinir:
    print("Tebrikler:" + magaza_adi + " promosyon kazandiniz!")
elif gelir < sinir:
    print("Uyarı! Cok dusuk gelir:" + str(gelir))
else:
    print("Takibe devam")    
    

# DONGULER - for

ogrenci = ["ali","veli","isik","berk"] 

ogrenci[0]
ogrenci[1]
ogrenci[2]
ogrenci[3]

for i in ogrenci :
    print(i)
    
# 

maaslar = [1000,2000,3000,4000,5000]

for i in maaslar:
    print(i)
    
# dongu ve fonksiyonlar birlikte

maaslar = [1000,2000,3000,4000,5000]

# maaslara %20 zam yapılacaktır 

def yeni_maas(x):
    print(x*20/100+x)
    
for i in maaslar:
    yeni_maas(i)
 
#uygulama

maaslar = [1000,2000,3000,4000,5000]
yeni_maas = []
def maas_ust(x):
    return x*10/100 + x
    
def maas_alt(x):
    return x*20/100 + x  

for i in maaslar:
    if i >= 3000 :
       # maas_ust(i)
        yeni_maas.append(maas_ust(i))
    else :
        #maas_alt(i)
        yeni_maas.append(maas_alt(i))
print(yeni_maas)

#break & continue

maaslar = [8000,5000,2000,1000,3000,7000,1000]

dir(maaslar)

maaslar.sort()
maaslar

for i in maaslar:
    if i == 3000:
        print("kesildi")
        break # islemi bitirmek dönguyu kesmek
    print(i)

for i in maaslar:
    if i == 3000:
        print("kesildi")
        continue # istenen degeri yakalayınca  onu atlar
    print(i)

#while

sayi = 1

while sayi<10:
    sayi += 1
    print(sayi)


def harf_say(x):
    return len(x)
 
harf_say("Merhaba!")

len("Merhaba!")

[1,2,3,4][2] == 2

#NESNE YONELIMLI PROGLAMLAMA

# Sinif Nedir? 



# Sinif Ozellikleri (Class attributes)

class VeriBilimci():
    bolum = ''
    sql = 'Evet'
    deneyim_yili = 0
    bildigi_diller = []

#Sınıfların Ozelliklerini erismek   

VeriBilimci.bolum
VeriBilimci.deneyim_yili

#Sınıfların ozelliklerini degistirmek

VeriBilimci.sql = "Hayır"    
VeriBilimci.sql

# Sinifin Orneklendirmesi (instantiation)

ali = VeriBilimci()

ali.sql
ali.deneyim_yili

ali.bildigi_diller.append("Python")  #burda eklenen bütün sınıfa eklenmektedir
ali.bildigi_diller

veli = VeriBilimci()

veli.sql
veli.bildigi_diller 

#Ornek ozellikleri

class VeriBilimci():
    bildigi_diller = ["R","Pyhton"]
    bolum = ''
    sql = ''
    deneyim_yili = 0
    def __init__(self): # Orneklemleri Temsil Eder Temsilci
        self.bildigi_diller = []
        self.bolum = ''
        
        
ali = VeriBilimci()
ali.bildigi_diller
ali.bildigi_diller.append("Python") #sadece bildigi dil
ali.bildigi_diller

veli = VeriBilimci()
veli.bildigi_diller
veli.bildigi_diller.append("MATLAB") # Sadece bildigi dil
veli.bildigi_diller

VeriBilimci.bolum
ali.bolum
ali.bolum ="istatistik"

VeriBilimci.bolum
veli.bolum = 'end'
ali.bolum
veli.bolum 
VeriBilimci.bolum

#Ornek Metodları

class VeriBilimci():
    calisanlar = [] 
    def __init__(self): # Orneklemleri Temsil Eder Temsilci
        self.bildigi_diller = []
        self.bolum = ''
    def dil_ekle(self, yeni_dil):
        self.bildigi_diller.append(yeni_dil)

ali = VeriBilimci()
ali.bildigi_diller
ali.bolum

veli = VeriBilimci()
veli.bildigi_diller
veli.bolum

dir(VeriBilimci())

VeriBilimci.dil_ekle
VeriBilimci.dil_ekle('python') #hata aldık

ali.dil_ekle("R")
ali.bildigi_diller

veli.dil_ekle("B")
veli.bildigi_diller

#Miras Yapilari (inheritance)

class Employess():
    def __init__(self):
        self.FirsName = ""
        self.LastName = ""
        self.Address = ""
        
class DataScience():
    def __init__(self): 
        self.Programming = ""

veribilimci1 = DataScience()
veribilimci1.Address

        
class Marketing():
    def __init__(self): 
        self.StoryTelling = ""

mar1 = Marketing()
mar1.

class Employess():
    def __init__(self,F):
        self.FirsName = ""
        self.LastName = ""
        self.Address = ""


# YAN etki : Bagımsızlık

A = 9

def impure_sum(b):
    return b + A

def pure_sum(a,b):
    return b + a


impure_sum(5)

pure_sum(3,4)


# ISimsiz Fonksiyonlar (Anonymous Functions)

def old_sum(a,b):
    return a + b

old_sum(4,5)

new_sum = lambda a,b: a + b
new_sum(4, 5)

sirasiz_liste = [('b',3),('a',8),('d',12),('c',1)]
sirasiz_liste

sorted(sirasiz_liste, key = lambda x: x[1])

# Vekterol Operatörler

import numpy as np
a = np.array([1,2,3,4])
b = np.array([2,3,4,5])


a*b

# map filter raduce

liste =  [1,2,3,4,5]

for i in liste:
    print(i+10)

list(map(lambda x: x+10, liste)) # verilen bir nesenin ısımsız tanımlanacak fonksiyonu yapar 


# filter

liste = [1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x : x % 2 ==0 ,liste))
#şartı saglanan elemanları geri dondurur

#reduce

from functools import reduce

liste = [1,2,3,4]

reduce(lambda a,b: a + b, liste)

#Hatalar / istisnalar (exceptions)

# ZeroDivisionErro hatası
a = 10
b= 0

a/b

try :
    print(a/b)
except ZeroDivisionError:
    print("Paydada sıfır olmaz")

#tip

a = 10 
b ="2"

a / b

try :
    print(a/b)
except TypeError:
    print("Sayı ve string")



#tip

a = 10 
b =2 

a / b

try :
    print(a/b)
except TypeError:
    print("Sayı ve string")



A = [1,2,3,4,5]

type(A)


import numpy as np
a = np.array([1,1,1])
b = np.array([2])
 
a+b




A = ["ali","veli","isik"]
B = [1,2,3]
AB = [A,B]
AB














