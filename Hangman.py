import random

word_list = ['watermelon']
word = random.choice(word_list)

guessed = False

print('Welcome to Hangman!')
print('Guess the word:')
print('-' * len(word))

guessed_letters = []

while not guessed:
    guess = input("Please guess a letter: ").lower()

    if guess in guessed_letters:
        print("You have already guessed that letter. Try again:")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(f"That's correct! '{guess}' is in the word.")

        word_so_far = ''
        for letter in word:
            if letter in guessed_letters:
                word_so_far += letter
            else:
                word_so_far += '-'

        print(word_so_far)

        if word_so_far == word:
            guessed = True
    else:
        print(f"Sorry, '{guess}' is not in the word.")

if guessed:
    print('You guessed the word! Congratulations!')
else:
    print('You have run out of attempts. The word was "watermelon". Better luck next time!')