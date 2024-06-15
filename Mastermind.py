def get_number_from_player(player):
    while True:
        number = input(f"Player {player}, enter your multi-digit number (at least 1 digit): ")
        if number.isdigit() and len(number) > 0:
            return number
        print("Invalid input. Please enter a multi-digit number.")

def get_guess_from_player(player, length):
    while True:
        guess = input(f"Player {player}, enter your guess (exactly {length} digits): ")
        if guess.isdigit() and len(guess) == length:
            return guess
        print(f"Invalid input. Please enter a {length}-digit number.")

def provide_hint(secret, guess):
    correct_position = 0
    correct_digit = 0
    
    secret_checked = [False] * len(secret)
    guess_checked = [False] * len(guess)
    
    
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            correct_position += 1
            secret_checked[i] = True
            guess_checked[i] = True
    
   
    for i in range(len(secret)):
        if not secret_checked[i]:
            for j in range(len(guess)):
                if not guess_checked[j] and secret[i] == guess[j]:
                    correct_digit += 1
                    guess_checked[j] = True
                    break
    
    return correct_position, correct_digit

def play_round(secret, player):
    guesses = 0
    while True:
        guess = get_guess_from_player(player, len(secret))
        guesses += 1
        if guess == secret:
            print(f"Player {player} guessed the number in {guesses} tries!")
            return guesses
        correct_position, correct_digit = provide_hint(secret, guess)
        print(f"Correct digits in the correct position: {correct_position}")
        print(f"Correct digits in the wrong position: {correct_digit}")

def main():
    print("Welcome to the Mastermind Game!")
    
    
    player1_number = get_number_from_player(1)
    print("\n" * 50) 
    
    
    player2_guesses = play_round(player1_number, 2)
    
    
    print("\n" * 50)  
    player2_number = get_number_from_player(2)
    print("\n" * 50)  
    
    
    player1_guesses = play_round(player2_number, 1)
    
    
    if player1_guesses < player2_guesses:
        print("Player 1 wins and is crowned Mastermind!")
    elif player2_guesses < player1_guesses:
        print("Player 2 wins and is crowned Mastermind!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
