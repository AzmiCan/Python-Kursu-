dosya = open("odev.txt", "r")
dizi = dosya.readlines()
dosya2 = open("cıktı.txt","w") #çıkış dosyası
for words in dizi:
    newWord = ""
    for harf in words:

        if (ord(harf) > 64 and ord(harf) < 91):
            """print(ord(harf))
            print(harf)"""
            newWord = newWord + harf

        elif (ord(harf) > 96 and ord(harf) < 123):
            """print(ord(harf))
            print(harf)"""
            newWord = newWord + harf
        else:

            """print(ord(harf))
            print(harf)"""
            newWord = newWord + ""
    dosya2.writelines([newWord,"\n"])
print(dosya2)
