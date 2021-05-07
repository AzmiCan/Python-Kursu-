####    Soru 1    ####

while True:
    user_input = input("Pozitif bir sayı giriniz: ")
    if user_input.isnumeric() == True :
        user_input = int(user_input)
        if user_input>0 :
            x = user_input
            break         
if user_input % 2 ==0 :
    print("girilen sayı çift")
else :
    print("girilen sayı tek")
    
    
###     Soru 2     ###

   
a = input("1.Sayıyı Giriniz: ")
b = input("2.Sayıyı Giriniz:  ")
c = input("3.Sayıyı Giriniz:  ")
d = input("4.Sayıyı Giriniz:  ")
e = input("5.Sayıyı Giriniz:  ")

x = [a,b,c,d,e]
y = []

for i in x:
    
    while True:
        if i.isnumeric()==True:
            i=int(i)
            if i>0:
                y.append(i)
                break
        else :
            print("Yanlış sayı girdin reis artık olduğu kadarıyla işlem yapacağız ")
            break
print("Girilen Sayılar:{}".format(y))

for j in y:

    if  j > 1:
       
       for i in range(2,j):
           if (j % i) == 0:
               print(j," Asal Sayı Değildir.")
               break
       else:
           print(j," Asal Sayıdır.")
     
    else:
       print(j," Asal Sayı Değildir.")
        
###     Soru 3    ###


  
ilk_string ="Ah5me4t"
ikinci_string = "M9eHm4eT"
ucuncu_string ="Ha3K5a1n"
def TemizVeri(a):
   
    
    x = ["1","2","3","4","5","6","7","8","9"]
    
    for i in a :
        
        for j in x :
             
            if i == j :
                a = a.replace(i,"")
    a = a.lower()
    a = a.title()
    return  a
print(TemizVeri(ilk_string)+"-"+TemizVeri(ikinci_string)+"-"+TemizVeri(ucuncu_string))
                
         
 



