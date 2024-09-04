import random
print("SAYI TAHMİN OYUNUMUZA HOS GELDİNİZ")
Lider_tablosu={}
def play_game():
    Takma_ad = input("Takma ad girin:")
    if Takma_ad in Lider_tablosu:
        puan=Lider_tablosu[Takma_ad]

play_game()

print("zorluk seviyesi seciniz: ")
print("kolay (1-10 arası 10p)")
print("orta (1-50 arası 25p)")
print("zor (1-100 arası 50p)")


secim = int(input("secimler (1/2/3)"))
if secim == 1:
    en_buyuk_sayi = 10
    puan = 10
elif secim == 2:
    en_buyuk_sayi =50
    puan = 25
elif secim == 3:
    en_buyuk_sayi = 100
    puan = 100
else:
    print("yanlıs secim yaptınız.")



tahmin = random.randint(1,100)
deneme_hakki = 5

while deneme_hakki > 0:

    tahmin = int(input(f"1 ile en büyük sayi arasında tahmin ediniz: "))
if tahmin == secim:
    print("dogru tahmin tebrikler!")
    toplam_puan += puan

elif tahmin < secim:
    print("sayıyı yükseltiniz!")
else:
    print("daha düşük sayi giriniz")
    deneme_hakki -= 1
if tahmin != secim:
    print(f"yanlıs tahmin")


