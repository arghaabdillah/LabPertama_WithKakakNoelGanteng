import random

# List of secret words
secret_words = [
    "nasi padang",
    "ayam suir",
    "rendang",
    "sate ayam",
    "gudeg",
    "bakso",
    "mie goreng",
    "pizza",
    "burger",
    "sushi"
]

# Global variables for score tracking
wins = 0
losses = 0

def play_hangman():
    global wins, losses

    if not secret_words:
        print("Tidak ada kata tersisa untuk dimainkan!")
        return False

    # Pick a random word and remove it from the list
    secret_word = random.choice(secret_words)
    secret_words.remove(secret_word)

    guessed_letters = ""
    chance = 6  # Standard hangman has 6 chances

    print("Game Hangman by Argha")
    print("Kata rahasia memiliki", len(secret_word), "karakter")

    while chance > 0:
        letter = input("Masukkan satu huruf: ")

        # Check valid input
        if len(letter) != 1 or not letter.isalpha():
            print("Input harus satu huruf!")
            continue

        letter = letter.lower()

        # Check if letter already guessed
        if letter in guessed_letters:
            print("Huruf sudah ditebak!")
            continue

        guessed_letters += letter

        # Check if letter is correct
        if letter in secret_word:
            print("Benar!")
        else:
            chance -= 1
            print("SALAH! Sisa kesempatan:", chance)

        # Display current state
        display_word = ""
        for char in secret_word:
            if char == " ":
                display_word += " "
            elif char in guessed_letters:
                display_word += char
            else:
                display_word += "_"

        print("Kata:", display_word)

        # Check if won
        if "_" not in display_word:
            print("Selamat! Kata berhasil ditebak:", secret_word)
            wins += 1
            return True

    # Lost the game
    print("Game over! Kata rahasia adalah:", secret_word)
    losses += 1
    return True

# Main game loop
while True:
    if not play_hangman():
        break

    # Display current score
    print(f"\nSkor saat ini - Menang: {wins}, Kalah: {losses}")

    # Ask to play again
    while True:
        choice = input("Apakah ingin bermain lagi? (y/n): ").lower()
        if choice == 'y':
            break
        elif choice == 'n':
            print(f"\nSkor akhir - Menang: {wins}, Kalah: {losses}")
            print("Terima kasih telah bermain!")
            exit()
        else:
            print("Masukkan y atau n!")

print(f"\nSkor akhir - Menang: {wins}, Kalah: {losses}")
print("Terima kasih telah bermain!")
