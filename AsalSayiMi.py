
sayi=int(input("Bir sayi giriniz:"))
kontrol=1
if sayi==1:
    kontrol=0
for i in range(2,sayi):
    if sayi%i==0:
        kontrol=0
        break
   
if kontrol==1:
    print(f"{sayi} sayisi ASALDİR.")
else:
    print(f"{sayi} sayisi ASAL DEGİLDİR.")
