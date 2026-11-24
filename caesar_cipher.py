def encrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha() and char.isascii():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + key) % 26 + base)
            result += new_char
        else:
            result += char

    return result


def decrypt(text, key):
    return encrypt(text, -key)


message = input("Enter your text: ")
key = int(input("Enter the key: "))

encrypted = encrypt(message, key)
print("Encrypted text:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted text:", decrypted)
