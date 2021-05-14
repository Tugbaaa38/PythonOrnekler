
#ekrandan okunan sayinin rakamlari toplamini bulan program

toplam=0
sayi=int(input("Sayi giriniz:"))
strSayi=str(sayi)     #burada sayiyi stringe cevirmemizin mantıgı her rakama kolayca ulasmak.

for rakam in strSayi:
    toplam+=int(rakam)

print("Girilen sayinin rakamlari toplami={}".format(toplam))

#baska bir yontemle daha yapalim
sayi2=int(input("Sayi giriniz:"))
toplam2=0
while gecici>0:
    basamak=gecici%10
    toplam2+=basamak
    gecici//=10

print("Girilen sayinin rakamlari toplami={}".format(toplam2))
