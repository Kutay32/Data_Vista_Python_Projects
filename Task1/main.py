import random
import csv

# Kullanıcı puanlarını saklamak için bir CSV dosyası
LEADERBOARD_FILE = 'leaderboard.csv'

# Kullanıcının puanını güncelleyen fonksiyon
def update_leaderboard(nickname, score):
    leaderboard = []
    try:
        with open(LEADERBOARD_FILE, mode='r') as file:
            reader = csv.reader(file)
            leaderboard = list(reader)
    except FileNotFoundError:
        pass

    for row in leaderboard:
        if row[0] == nickname:
            row[1] = str(int(row[1]) + score)
            break
    else:
        leaderboard.append([nickname, str(score)])

    with open(LEADERBOARD_FILE, mode='w') as file:
        writer = csv.writer(file)
        writer.writerows(leaderboard)

# Leaderboard'u gösteren fonksiyon
def display_leaderboard():
    try:
        with open(LEADERBOARD_FILE, mode='r') as file:
            reader = csv.reader(file)
            leaderboard = sorted(list(reader), key=lambda x: int(x[1]), reverse=True)

        print("\n-- En İyi 5 Oyuncu --")
        for i, row in enumerate(leaderboard[:5], start=1):
            print(f"{i}. {row[0]}: {row[1]} puan")
    except FileNotFoundError:
        print("Leaderboard henüz oluşturulmadı.")

# Oyunun ana fonksiyonu
def play_game(nickname):
    print("Zorluk seviyesini seçin:")
    print("1. Kolay (1-10 arası)")
    print("2. Orta (1-50 arası)")
    print("3. Zor (1-100 arası)")

    try:
        difficulty = int(input("Seçiminiz (1/2/3): "))
    except ValueError:
        print("Lütfen geçerli bir sayı girin!")
        return

    if difficulty == 1:
        max_number = 10
        points = 10
    elif difficulty == 2:
        max_number = 50
        points = 25
    elif difficulty == 3:
        max_number = 100
        points = 50
    else:
        print("Geçersiz seçim!")
        return

    secret_number = random.randint(1, max_number)
    attempts = 5

    while attempts > 0:
        try:
            guess = int(input(f"1 ile {max_number} arasında bir sayı tahmin edin: "))
        except ValueError:
            print("Lütfen geçerli bir sayı girin!")
            continue

        if guess == secret_number:
            print(f"Tebrikler! Doğru tahmin ettiniz. {points} puan kazandınız.")
            update_leaderboard(nickname, points)
            break
        elif guess < secret_number:
            print("Daha büyük bir sayı girin.")
        else:
            print("Daha küçük bir sayı girin.")

        attempts -= 1
        print(f"Kalan tahmin hakkı: {attempts}")

    if attempts == 0:
        print("Tahmin hakkınız bitti! Doğru sayı:", secret_number)

    display_leaderboard()

# Yeniden oynama fonksiyonu
def main():
    nickname = input("Nickname'inizi girin: ").strip()

    while True:
        play_game(nickname)

        again = input("Yeniden oynamak ister misiniz? (E/H): ").strip().lower()
        if again != 'e':
            print("Oyun bitti, görüşmek üzere!")
            break

if __name__ == "__main__":
    main()
