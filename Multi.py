def encrypt(text, key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            mychar = ord(char) - 65
            ans = (mychar * key) % 26
            result += chr(ans + 65)
        else:
            mychar = ord(char) - 97
            ans = (mychar * key) % 26
            result += chr(ans + 97)

    return result


text = input("Enter your text: ")
key = int(input("Enter key: "))
print("Text : " + text)
print("key : " + str(key))
print("Cipher : " + encrypt(text, key))
