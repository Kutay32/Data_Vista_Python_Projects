import random
import csv
Lider_tablosu={}
def play_game():
    Takma_ad = input("Takma ad girin:")
    if Takma_ad in Lider_tablosu:
        score=Lider_tablosu[Takma_ad]
        print("Hoşgeldin,{Takma_ad} Mevcut puan:{score}")
    else:
        Lider_tablosu[Takma_ad]=score 
    print("Zorluk seviyesi seçin:")
    print("1.kolay (1-10)")
    print("2.orta (1-50)")
    print("3.zor (1-100)")
    Seçiminiz=int(input("Seçiminiz (1,2,3:)"))
    if seçim == 1:
        max_sayı = 1 
        doğru_tahmin = 10 
    elif seçim == 2:
        max_sayı = 50 
        dogru_tahmin = 25
    elif seçim == 3:
        max_sayı =100 
        doğru_tahmin = 50 
    else:
        print("Hatalı seçim")
    doğru_tahmin=random.randint(1,max_sayı)
    for hak in range(5)
        guess=int(input(f"{hak+1} Tahmininizi gir (1-{max_number}:"))
        if tahmin == doğru_tahmin:
            print(f"Tebrikler,doğru tahmin.{puan} puan kazandınız")
            score += puan
            Lider_tablosud[Takma_ad] = score
            break 
        elif tahmin < doğru_tahmin:
            print("Daha yüksek bir sayı söyleyin")
        else:
            print("Daha düşük bir sayı söyleyin")
        if tahmin != doğru_tahmin:
            print(f"yanlış bildiniz,doğru sayı {correct_guess}")
            
            
        
