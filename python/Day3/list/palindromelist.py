def palindrome(word):
    return word == word[::-1]

def take_input():
    sentence = input("Enter a sentence: ")
    wordsList = []
    word = ""
    for char in sentence:
        if char != " ":
            word += char
        else:
            if word:
                wordsList.append(word)
                word = ""
    if word:
        wordsList.append(word)
    return wordsList

def main():
    wordsList = take_input()
    for word in wordsList:
        if palindrome(word):
            print(f"'{word}' is a palindrome")
        else:
            print(f"'{word}' is not a palindrome")

main()