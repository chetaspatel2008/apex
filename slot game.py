import random


def spin_row():
    symbol = ['🍎', '🍌', '🍒', '🍣', '🍇']
    results = [random.choice(symbol) for _ in range(3)]

    return results


def print_row(row):
    print("***********")
    print(" | ".join(row))
    print("***********")


def winning(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍎':
            return bet * 3

    if row[0] == row[1] == row[2]:
        if row[0] == '🍌':
            return bet * 4

    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 5  
    
    if row[0] == row[1] == row[2]:
        if row[0] == '🍣':
            return bet * 6  
    
    if row[0] == row[1] == row[2]:
        if row[0] == '🍇':
            return bet * 7 
        
    if row[0] == row[1] != row[2]:
        if row[0] == '🍎':
            return bet * 2
    
    if row[0] == row[1] != row[2]:
        if row[0] == '🍌':
            return bet * 2
    if row[0] == row[1] != row[2]:
        if row[0] == '🍒':
            return bet * 2
    if row[0] == row[1] != row[2]:
        if row[0] == '🍣':
            return bet * 2
    if row[0] == row[1] != row[2]:
        if row[0] == '🍇':
            return bet * 2
        
    if row[0] != row[1] == row[2]:
        if row[1] == '🍎':
            return bet * 2
    
    if row[0] != row[1] == row[2]:
        if row[1] == '🍌':
            return bet * 2
    
    if row[0] != row[1] == row[2]:
        if row[1] == '🍒':
            return bet * 2
    
    if row[0] != row[1] == row[2]:
        if row[1] == '🍣':
            return bet * 2
    
    if row[0] != row[1] == row[2]:
        if row[1] == '🍇':
            return bet * 2
    else:
        return 0
def main():

    balance = 100 
    
    print("***************************")
    print("Welcome player to the GAME")
    print("Symbols : 🍎 🍌 🍒 🍣 🍇 ")
    print("***************************")
    
    while balance > 0:
        print(f"Your cutrrent balance is ₹{balance}")
        
        bet = input("Enter your bet amount : ")

        if not bet.isdigit():
            print("Enter a valid amount in digit")
            continue
        bet = int(bet)
        

        if bet > balance :
            print("Insufficient amount")
            continue


        if bet <= 0 :
            print("Bet should be greater than 0")
            continue

        balance -= bet
        
        import time
        row = spin_row()
        print("Spining.....\n")
        for x in range (2):
            seconds = x % 60 
        time.sleep(2)
        print_row(row)
        win = winning(row,bet)
        
        if win > 0:
            print ("**************************")
            print(f" TADAAA!!! you win ₹{win}")

        else:
            print ("**************************")
            print("You lost, better luck next time !!")
        
        balance = balance + win
        print(f"Your curent balance is total {balance}")
        print ("**************************")
        
        play_again = input("do you want to play again (Y/N): ")
             
        if play_again != 'Y' :
            print("Thanks for playing 😊")
            break
        
if __name__ == '__main__' :
    main()
