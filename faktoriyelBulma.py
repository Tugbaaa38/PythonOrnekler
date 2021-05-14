sayi=int(input("Bir sayi giriniz:"))
fak=1
while sayi>0:         
    fak*=sayi
    sayi-=1

print("Girdiginiz sayinin faktoriyeli={}".format(fak))
print(f"Girilen sayinin faktoriyeli={fak}")


#Burada da for dongusu ile faktoriyel bulduk.
sayi2=int(input("Bir sayi giriniz:"))
fak2=1
for i in range(1,sayi2+1):
    fak2*=i
   
print(f"{sayi2}!={fak2}")



