import random 
word = ["chair","tiger","gredy","ruchi","table"]
secret_word = random.choice(word)
display = ['_'for _ in secret_word]
guessed_word = []
max_guesses = 6
wrong_guesses = 0
while True:
    print("current word: ", ' '.join(display))
    print(f"wrong guesses left: {max_guesses - wrong_guesses}")
    print(f"guessed word: { ','.join(guessed_word)}\n")
    
    guess = input("Enter a letter: ").lower()
    if not guess.isalpha() or len(guess)!=1:
        print(" enter a single alphabet letter.\n")
        continue
    if guess in guessed_word:
        print("you've already gussed that letter.try another one.😒\n")
        continue
    guessed_word.append(guess)

    if guess in secret_word:
        print("correct guess| 😁\n")
        for index, letter in enumerate(secret_word):
            if letter == guess:
                display[index] = guess
    else:
        print("wrong guess|\n")
        wrong_guesses +=1
    if '_' not in display:
        print(" congratulations🤌🎉| you gussed the word:",secret_word)
        break
    if wrong_guesses >= max_guesses:
        print("game over! you ran out of guesses.😔")
        print("the correct word was:",secret_word)  
        break

        

