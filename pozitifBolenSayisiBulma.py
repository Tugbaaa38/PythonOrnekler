#ekrandan okunan sayinin kac tane pozitif boleni oldugunu bulan program

bolenSayisi=0
sayi=int(input("Sayi giriniz:"))

for i in range(1,sayi+1):
    if sayi%i==0:
        bolenSayisi+=1

print(f"{sayi} sayisinin {bolenSayisi} tane pozitif boleni vardir.")
