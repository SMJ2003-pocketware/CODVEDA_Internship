#NUMBER GUESSING GAME
#Name:Soham Majumder

#importing the required dependencies
import random
#creating the function 
def start_game():
    #we allowing the player/user to choose the difficulty at which he wants to play the game
    print("Select the difficulty level (easy, medium, hard) at which you want to play the game")
    difficulty=input("Select difficulty level:").lower() 
    #the number of attempts the player/user gets depends on the difficulty level that they choose
    if difficulty=="easy":
        max_attempts=10
    elif difficulty=="medium":
        max_attempts=7
    elif difficulty=="hard":
        max_attempts=5
    else:
        print("Invalid choice")
        print("Setting the difficulty to medium by default")
        max_attempts=7

    #To generate a random number between the range of (1-100)
    target_number=random.randint(1, 100)
    attempts=0
    print("Welcome to the Number Guessing Game!\nTry to guess the correct number between 1 and 100")
    print(f"You have {max_attempts} attempts. Good luck!")

    while attempts<max_attempts:
        try:
            guess=int(input("Enter your guess:"))
            attempts+=1
            if guess<target_number:
                print("Too low")
            elif guess>target_number:
                print("Too high")
            else:
                print(f"Congratulations!You've guessed the number {target_number} in {attempts} attempts")
                break
        except ValueError:
            print("That's not a valid number.Please enter a valid input")
    if attempts==max_attempts:
        print(f"Game over!You've used all {max_attempts} attempts.The number was {target_number}.Better luck next time!")

# Start the game
start_game()
