
#ekrandan okunan sayinin rakamlari toplamini bulan program

toplam=0
sayi=int(input("Sayi giriniz:"))
strSayi=str(sayi)     #burada sayiyi stringe cevirmemizin mantıgı her rakama kolayca ulasmak.

for rakam in strSayi:
    toplam+=int(rakam)

print("Girilen sayinin rakamlari toplami={}".format(toplam))