import random  
import csv 
leader_board={}
def number_guessing_game():  
    nickname=input("what is your nickname?") 
if nickname in leaderboard:   
    score=leader_board[nickname]
    print(f"welcome{nickname},your score is {score}") 
else:  
    print(f"welcome{nickname}",your score is 0") 
    score=0  
    
print("the game should have three difficulty levels:") 
print("level1:easy:guess numbers between 1 to 10 including 1and 10") 
print("level2:medium:guess numbers between 1 to 50 including 1 and 50") 
print("level3:hard:guess numbers between 1 to 100 including 1and 100") 
level=input("which level do you want to play?say: 1,2 or 3")    
  
tahmin_hakki=5
 
if level==1 :  
    asil_sayi=random.randint(1,10)  
    if asil_sayi==tahmin: 
         score+=10  
    else: 
         score+=0
elif level ==2:      
    asil_sayi=random.randint(1,50)  
    if asil_sayi==tahmin: 
        score+=25 
    else: 
         score+=0
else:   
    asil_sayi=random.randint(1,100)  
    if asil_sayi==tahmin: 
        score+=50 
    else: 
        score+=0
     
while tahmin_hakki>0:  
        tahmin=int(input("i picked a number within the range u choose, guess it")) 
       if tahmin==asil_sayi: 
           print("correct guess!") 
    break  
       elif tahmin> asil_sayi:  
           print("enter a smaller number!") 
       else : 
           print("enter a bigger number!") 
     
    global tahmin_hakki
    tahmin_hakki-=1  
        
if tahmin_hakki==0: 
        print(f"you've run out of guesses!correct guess:{asil_sayi} ")  
 
number_guessing_game()
