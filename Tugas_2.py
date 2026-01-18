secret_word = "ayam suir"
guessed_letters = ""
chance = 3
print("Game Tebak Kata by Argha")

while chance > 0:
    letter = input("Masukkan satu huruf: ")

    # cek input valid
    if len(letter) != 1 or not letter.isalpha():
        print("Input harus satu huruf!")
        continue

    letter = letter.lower()

    # cek huruf benar atau salah
    if letter in secret_word:
        guessed_letters += letter
    else:
        chance -= 1
        print("SALAH KOCAK!! Sisa kesempatan:", chance)

    # tampilkan kata
    display_word = ""
    for char in secret_word:
        if char == " ":
            display_word += " "
        elif char in guessed_letters:
            display_word += char
        else:
            display_word += "_"

    print(display_word)

    # cek selesai
    if "_" not in display_word:
        print("Selamat! Kata berhasil ditebak:", secret_word)
        break