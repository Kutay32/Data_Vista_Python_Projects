import random
import csv
Lider_tablosu={}
def play_game():
    Takma_ad=input("Takma ad gir:")
    if Takma_ad in Lider_tablosu:
        score=Lider_tablosu[Takma_ad]
        print("Hoşgeldin,{Takma_ad} Mevcut puan:{score}")
    else:
        Lider_Tablosu[Takma_ad]=score
    print("Zorluk seviyesi seçin:")
    print("1.kolaya (1-10")
    print("2.orta (1-50)")
    print("3.zor (1-100)")
    Seçiminiz=int(input("Seçiminiz (1,2,3)"))
    if seçim == 1:
        max_sayı = 1
        doğru_tahmin = 10
    elif seçim == 2:
        max_sayı = 50
        doğru_tahmin = 25
    else:
        print("Hatalı seçim")
    doğru_tahmin=random.randint(1,max_sayı)
    for hak in range(5):
        guess=int(input(f" {hak+1} Tahmininizi girin (1-{max_number}:"))
        if tahmin == doğru_tahmin:
            print(f"Tebrikler, doğru tahmin, {puan} puan kazanndınız")
            score += puan
            Lider_tablosu[Takma_ad]=score
            break
        elif tahmin < doğru_tahmin:
            print("Daha yüksek bir sayı söyleyin ")
        else:
            print("Daha düşük bir sayı söyleyin ")
        if tahmin != doğru_tahmin:
            print(f"yanlış bildiniz,doğru sayı {doğru_tahmin}")
            import csv


     def get_score(Takma_ad):
            try:
                with open('leaderboard.csv', mode='r', newline='') as file:
                     reader = csv.reader(file)
                    for row in reader:
                         if row[0] == nickname:
                            return int(row[1])
            except FileNotFoundError:
                pass
                return 0

            # Kullanıcı adını ve yeni skorunu dosyaya kaydet
         def update_score(nickname, score):
                scores = []
             updated = False
                try:
                    with open('leaderboard.csv', mode='r', newline='') as file:
                        reader = csv.reader(file)
                        for row in reader:
                            if row[0] == nickname:
                                scores.append([nickname, score])
                                updated = True
                            else:
                                scores.append(row)
                except FileNotFoundError:
                    pass

                if not updated:
                    scores.append([nickname, score])

                with open('leaderboard.csv', mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(scores)

            # En yüksek 5 skoru göster
            def display_top_scores():
                try:
                    with open('leaderboard.csv', mode='r', newline='') as file:
                        reader = csv.reader(file)
                        scores = sorted(reader, key=lambda x: int(x[1]), reverse=True)
                        print("En İyi 5 Skor:")
                        for row in scores[:5]:
                            print(f"{row[0]}: {row[1]}")
                except FileNotFoundError:
                    print("Henüz skor yok.")
