import random

def choose_word():
    words = ['python', 'hangman', 'challenge', 'developer', 'programming']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6
    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\nWord: ", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            print("Good guess!")
            guessed_letters.append(guess)
        else:
            print("Wrong guess!")
            attempts -= 1
            guessed_letters.append(guess)
            print(f"You have {attempts} attempts left.")
        
        if display_word(word, guessed_letters) == word:
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        print(f"Game Over! The word was: {word}")

if __name__ == "__main__":
    hangman()
