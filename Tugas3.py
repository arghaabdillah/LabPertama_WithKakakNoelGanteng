def updateText(word, ketebak, guess):
    text = ''

    for letter in word:
        if letter in ketebak:
            text += letter + " "
        else:
            text += "_ "

    if guess in word:
        print(f"ternyata {guess} ada di dalam kata")
    else:
        print(f"woy, huruf {guess} ga ada di dalam kata")

    print(text)
    return text

def main(word):
    chances = 5
    ketebak = []
    text = ''

    for letter in word:
        text += "_ "

    print('hangman with argha')
    print("word:", text)

    while chances > 0 and "_" in text:
        guess = input("guess a letter: ")

        if not guess.isalpha() or len(guess) != 1:
            print("1 huruf aja, jangan maruk")
            continue

        guess = guess.lower()
        ketebak.append(guess)

        text = updateText(word, ketebak, guess)

        if guess not in word:
            chances -= 1
            print(f"you only have: {chances} chances left.")

    if '_' not in text:
        print("selamat pasep udah menebak kata dengan benar")
    else:
        print(f"LU KALAH AYAM")

main("papeda")