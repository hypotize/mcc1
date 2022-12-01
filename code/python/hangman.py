def showWord(word, guesses):
    show = ""
    for x in word:
        if x in guesses:
            show += x
        else:
            show += '*'
    return show

print('+----------------+')
print('| Guess the word |')
print('+----------------+')
word = "MIURASHI"

guesses  = ""
print(showWord(word, guesses))

complete = False

while complete == False:
    print ('Enter a letter:')
    guess = input().upper()
    if len(guess) > 1:
        guess = guess[0]
    if guess in guesses:
        print('aready guessed', guess)
    else:
        guesses += guess
        if guess in word:
            show = showWord(word, guesses)
            print(show) 
            if '*' not in show:
                complete = True
                print ('You win')
                print('It took you', len(guesses), 'guesses')
        else:
            print("Not found")
            print(showWord(word, guesses))


