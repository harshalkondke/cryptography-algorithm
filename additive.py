def encrypt(text, key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            if (ord(char) + key) > 90:
                ans = (ord(char) + key) - 90 + 64
                result += chr(ans)
            else:
                result += chr((ord(char) + key))
        else:
            if (ord(char) + key) > 122:
                ans = (ord(char) + key) - 122 + 96
                result += chr(ans)
            else:
                result += chr((ord(char) + key))

    return result


text = input("Enter your text: ")
key = int(input("Enter key: "))
print("Text : " + text)
print("key : " + str(key))
print("Cipher : " + encrypt(text, key))

