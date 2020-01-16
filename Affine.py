def affine_encrypt(text, key):

    # C = (a*P + b) % 26
    result = ""
    for t in text.upper().replace(' ', ''):
        equ = (int(key[0]) * (ord(t) - 65)) + int(key[1])
        ans = (equ % 26) + 65
        result += chr(ans)
    return result


def main():
    text = input("Enter Text: ")
    key = []
    for i in range(0, 2):
        s = input("Enter " + str(i) + " Key: ")
        key.append(s)

    encrypted_text = affine_encrypt(text, key)

    print('Encrypted Text: {}'.format(encrypted_text))


if __name__ == '__main__':
    main()
