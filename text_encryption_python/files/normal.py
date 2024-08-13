def encrypt(text, int_key, str_key):
    encrypted_text = ""
    str_key_index = 0
    for char in text:
        if char.isalpha():
            shift = (ord(str_key[str_key_index]) - ord('a') + int_key) % 26
            if char.isupper():
                encrypted_text += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
            str_key_index = (str_key_index + 1) % len(str_key)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, int_key, str_key):
    decrypted_text = ""
    str_key_index = 0
    for char in encrypted_text:
        if char.isalpha():
            shift = (ord(str_key[str_key_index]) - ord('a') + int_key) % 26
            if char.isupper():
                decrypted_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            str_key_index = (str_key_index + 1) % len(str_key)
        else:
            decrypted_text += char
    return decrypted_text


if __name__ == "__main__":
    text = input("Enter the text to encrypt: ")
    int_key = int(input("Enter the integer key: "))
    str_key = input("Enter the string key: ")

    encrypted_text = encrypt(text, int_key, str_key)
    print("Encrypted text:", encrypted_text)

    decrypted_text = decrypt(encrypted_text, int_key, str_key)
    print("Decrypted text:", decrypted_text)