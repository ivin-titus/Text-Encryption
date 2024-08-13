def derive_key(str_key):
    return sum(ord(char) for char in str_key)

def encrypt(text, int_key, str_key):
    encrypted_text = ""
    derived_key = derive_key(str_key)

    for char in text:
        encrypted_char = chr(ord(char) + derived_key + int_key)

        encrypted_text += encrypted_char

    return encrypted_text

def decrypt(encrypted_text, int_key, str_key):
    decrypted_text = ""
    derived_key = derive_key(str_key)

    for char in encrypted_text:
        decrypted_char = chr(ord(char) - derived_key - int_key)

        decrypted_text += decrypted_char

    return decrypted_text

if __name__ == "__main__":
    text = input("Enter the text to encrypt: ")
    int_key = int(input("Enter the integer key: "))
    str_key = input("Enter the string key: ")

    encrypted_text = encrypt(text, int_key, str_key)
    print("Encrypted text:", encrypted_text)
    
    decrypted_text = decrypt(encrypted_text, int_key, str_key)
    print("Decrypted text:", decrypted_text)
