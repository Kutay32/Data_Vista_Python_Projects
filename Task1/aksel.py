import random
import pandas as pd


def loadingFile(file_name='scoreboard.csv'):
    try:
        return pd.read_csv(file_name, index_col='Nickname') #CSV dosyasını pandas ile okur ve "Nickname" sütununu indeks olarak ayarlar. Böylece her oyuncunun puanına kolayca erişebiliriz.
    except FileNotFoundError:
        return pd.DataFrame(columns=['Nickname', 'Score']).set_index('Nickname')

def save_scoreboard(scoreboard, file_name='scoreboard.csv'):
    scoreboard.to_csv(file_name) # Mevcut skor tablosunu CSV dosyasına yazar.

def display_top_scores(scoreboard):
    top_5 = scoreboard.nlargest(5, 'Score') #Skor tablosundaki en yüksek 5 skoru bulur.
    print("\n Top 5 Scores ")
    print(top_5[['Score']])


def play_game():
    scoreboard = loadingFile()

    nickname = input("Enter your nickname: ") # Eğer oyuncunun takma adı skorbordda varsa, o oyuncunun mevcut skoru tablo üzerinden alınır.
    if nickname in scoreboard.index:
        score = scoreboard.loc[nickname, 'Score']
    else:
        score = 0



    print("\nChoose difficulty: 1. Easy (1-10), 2. Medium (1-50), 3. Hard (1-100)")
    difficulty = {'1': (10, 1, 10), '2': (25, 1, 50), '3': (50, 1, 100)}.get(input(), (10, 1, 10))
    points, low, high = difficulty
    target = random.randint(low, high)


    for attempt in range(5): #burada oyuncuya verilen 5 deneme hakkı için döngü kullanılmıştır.
        try:
            guess = int(input(f"Guess a number between {low} and {high}: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess == target:
            print("Correct!")
            score += points
            break
        print("Higher!" if guess < target else "Lower!")
    else:
        print(f"Out of attempts! The correct number was {target}.")

    scoreboard.loc[nickname] = score
    save_scoreboard(scoreboard)
    print(f"\n{nickname}'s total score: {score}")
    display_top_scores(scoreboard)

if __name__ == "__main__":
    play_game()




