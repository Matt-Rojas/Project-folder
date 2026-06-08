import random

word_bank = ["python", "programming", "developer", "algorithm", "function", "variable", "loop", "condition"]

# Select a random word from the word bank
word = random.choice(word_bank)
guessedWord = ['_'] * len(word)
attempts = 10

# Game loop
while attempts > 0:
    # Display the current state of the guessed word
    print("\nCurrent word: " + " ".join(guessedWord))
    guess = input('Guess a letter: ').lower()

    # Check if the guess is valid
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('Great guess!')
    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))
    
    # Check if the player has guessed the word
    if '_' not in guessedWord:
        print("\nCongratulations! You guessed the word: " + word)
        break

    # Check if the player has run out of attempts
    if attempts == 0 and '_' in guessedWord:
        print("\nYou ran out of attempts! The word was: " + word)
    

    