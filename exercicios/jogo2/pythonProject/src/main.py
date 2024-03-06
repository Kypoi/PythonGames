def load_words(file_path):
    words = []
    f = open(file_path, "r")
    for x in f:
        x = x.strip()
        words.append(x)
    return words


def detect_anagrams(words, user_word):
    anagrams = []
    for word in words:
        if sorted(word) == sorted(user_word):
            anagrams.append(word)
            print(word + " é anagrama")


def main():
    print("Bem-vindo ao Detetor de Anagramas!")
    while True:
        word = input("Escolha uma palavra: ")
        if word.isalpha():
            break
        else:
            print("Por favor, digite uma palavra válida contendo apenas letras do alfabeto.")
    words = load_words("./palavras.txt")
    detect_anagrams(words, word)


if __name__ == "__main__":
    main()
