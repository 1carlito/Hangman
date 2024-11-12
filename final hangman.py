import os, time, random

# Load words from the file
with open("dictionary.txt", "r") as file:
    contents = file.readlines()
    words = [line.strip() for line in contents]

# Choose a random word for the game
hangword = random.choice(words)
guessedletter = []
maxattempts = 9

print("\033[0;32m", "Welcome to Hangman!")


hidden = "".join("_ " for _ in hangword)



def viewguess():
   print("Guessed letters:", " ".join(guessedletter), "\n")


while True:
    
    hidden = "".join([letter if letter in guessedletter else "_ " for letter in hangword])
    print("Current Word:", hidden, "\n")  
    
    guess = input("Please choose a letter :>\n ").strip().lower()
    
  
    if guess in guessedletter:
        print("That guess has already been inputted")
        continue 

    
    guessedletter.append(guess)
    
    
    if guess in hangword:
        print("Correct guess! Well done!\n")
    else: 
        maxattempts -= 1
        print(f"Unlucky, that is incorrect :( You have {maxattempts} attempts remaining.\n")
    
    time.sleep(4)
    os.system("cls")
    
    if "_ " not in hidden:
        print(f"Congratulations! You've guessed the word - {hangword} - with {maxattempts} attempts remaining.")
        break
    elif maxattempts == 0:
        print(f"Unlucky, you're out of attempts! The word was {hangword}.")
        break

    
    viewguess()
