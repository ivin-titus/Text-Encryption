import sys

def decrypt(word, key):
    cypher = []

    for char in word:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - base + 26 - key) % 26 + base)
            cypher.append(decrypted_char)
        else:
            cypher.append(char)

    return ''.join(cypher)

def encrypt(word, key):
    cypher = []

    for char in word:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - base + key) % 26 + base)
            cypher.append(encrypted_char)
        else:
            cypher.append(char)

    return ''.join(cypher)

if __name__ == "__main__":
    use = input("Use (Encrypt or Decrypt): ")

    if use not in ["Encrypt", "Decrypt"]:
        print("Given Method Not Allowed - Allowed: Encrypt / Decrypt")
        sys.exit(3)

    key = int(input("Key: "))

    if key < 1:
        print("Key Must be greater than 0")
        sys.exit(4)

    word = input(f"Text you Want to {use}: ")

    if use == "Encrypt":
        result = encrypt(word, key)
    else:
        result = decrypt(word, key)

    print(f"{use}ed Text: {result}")
