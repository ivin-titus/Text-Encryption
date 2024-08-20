# **Text Encryption - Algorithm Explaination**

This is the algorithm level explaination of this project for further developments.
This project basically have `3 levels` of `encryption` and `decryption` and it includes `Simple`, `Normal` and `Advanced`. It basically uses **Caesar ciphers** for **[alphabet shifting](https://www.khanacademy.org/computing/computer-science/cryptography/ciphers/a/shift-cipher)**. I implimented it's more secured versions which have 2 - 3 keys and it **also works with [Unicode Characters](https://en.wikipedia.org/wiki/Unicode)**. Usually, pure Caeser cipher algoriths have only one key and it works with [ASCII Characters](https://www.techtarget.com/whatis/definition/ASCII-American-Standard-Code-for-Information-Interchange#:~:text=Characters%20in%20ASCII%20encoding%20include,use%20with%20teletype%20printing%20terminals.)


## **On Simple Level Encryption**

It's using basic Caeser cipher algorithm which have only one key

### 1. **Before Encryption**

- **Original Word:** "HELLO"
- Imagine each letter is on a scale from A to Z.

```
H  E  L  L  O
```

### 2. **Encryption Process**

- **Key:** 3
- Shift each letter forward by 3 positions in the alphabet:

```
H → K
E → H
L → O
L → O
O → R
```

- **Encrypted Word:** "KHOOOR"

### 3. **After Encryption**

- The letters have shifted to their new positions:

```
H  E  L  L  O  →  K  H  O  O  R
```

### 4. **Decryption Process**

- To decrypt, shift the letters back by the same key (3 positions):

```
K → H
H → E
O → L
O → L
R → O
```

- **Decrypted Word:** "HELLO"
---
<br>

## **On Normal Level Encryption** 

It's a customized cipher encryption algorithm made by me, which have 2 keys (1 integer + 1 string [alpha-numeric])

### 1. **Before Encryption**

- **Original Word:** Let's say the word is "HELLO".
- **Integer Key:** 3
- **String Key:** "abc" (repeated if needed)

### 2. **Encryption Process**

- Each letter in "HELLO" will be shifted by a combination of the integer key and the corresponding letter in the string key.
  
  - For **H** (1st letter) and **a** (1st letter of string key):
    - Shift by **3 (int key) + 0 ('a' - 'a') = 3**
    - **H → K**
  
  - For **E** (2nd letter) and **b** (2nd letter of string key):
    - Shift by **3 (int key) + 1 ('b' - 'a') = 4**
    - **E → I**
  
  - For **L** (3rd letter) and **c** (3rd letter of string key):
    - Shift by **3 (int key) + 2 ('c' - 'a') = 5**
    - **L → Q**
  
  - For **L** (4th letter) and **a** (1st letter of string key again):
    - Shift by **3 (int key) + 0 ('a' - 'a') = 3**
    - **L → O**
  
  - For **O** (5th letter) and **b** (2nd letter of string key again):
    - Shift by **3 (int key) + 1 ('b' - 'a') = 4**
    - **O → S**

- **Encrypted Word:** "KIOQS"

### 3. **After Encryption**

- The letters have been shifted to their new positions:

```
H  E  L  L  O  →  K  I  O  Q  S
```

### 4. **Decryption Process**

- To decrypt, reverse the shift by the same keys:

  - For **K** (1st letter) and **a** (1st letter of string key):
    - Shift back by **3 (int key) + 0 ('a' - 'a') = 3**
    - **K → H**
  
  - For **I** (2nd letter) and **b** (2nd letter of string key):
    - Shift back by **3 (int key) + 1 ('b' - 'a') = 4**
    - **I → E**
  
  - For **O** (3rd letter) and **c** (3rd letter of string key):
    - Shift back by **3 (int key) + 2 ('c' - 'a') = 5**
    - **O → L**
  
  - For **Q** (4th letter) and **a** (1st letter of string key again):
    - Shift back by **3 (int key) + 0 ('a' - 'a') = 3**
    - **Q → N**
  
  - For **S** (5th letter) and **b** (2nd letter of string key again):
    - Shift back by **3 (int key) + 1 ('b' - 'a') = 4**
    - **S → O**

- **Decrypted Word:** "HELLO"

<br>

---

## **On Advanced Level Encryption**


### 1. **Deriving the Key**

- **String Key:** "abc"
- **Derived Key Calculation:** The derived key is calculated by summing the Unicode values of the characters in the string key.

  - For "abc":
    - 'a' = 97
    - 'b' = 98
    - 'c' = 99
    - **Derived Key** = 97 + 98 + 99 = **294**

### 2. **Encryption Process**

- **Original Text:** "HELLO"
- **Integer Key:** 3
- **Derived Key:** 294 (from string key "abc")

To encrypt, shift each character in the text by adding the derived key and integer key:

- For **H**:
  - Unicode value of 'H' = 72
  - Shifted Unicode = 72 + 294 + 3 = 369
  - Encrypted Character = chr(369) = 'ý'
  
- For **E**:
  - Unicode value of 'E' = 69
  - Shifted Unicode = 69 + 294 + 3 = 366
  - Encrypted Character = chr(366) = 'ü'

- Repeat this process for each character, including any Unicode characters.

- **Encrypted Text:** The result will be a string of characters based on the Unicode values calculated.

### 3. **Decryption Process**

To decrypt, reverse the process by subtracting the derived key and integer key:

- **Encrypted Text:** For example, "ýü..."
- **Integer Key:** 3
- **Derived Key:** 294 (from string key "abc")

To decrypt, shift each character in the encrypted text backward by subtracting the derived key and integer key:

- For **ý**:
  - Unicode value of 'ý' = 369
  - Original Unicode = 369 - 294 - 3 = 72
  - Decrypted Character = chr(72) = 'H'
  
- For **ü**:
  - Unicode value of 'ü' = 366
  - Original Unicode = 366 - 294 - 3 = 69
  - Decrypted Character = chr(69) = 'E'

- Repeat this process for each character, including any Unicode characters.

- **Decrypted Text:** "HELLO"

<br>

---
## **Conclusion**

In this guide, we examined various methods for encrypting and decrypting text to protect information. Each technique follows the same core principle: transforming text into an unreadable format with a key and then reverting it back to its original form using the same key.

- **Basic Caesar Cipher (On Simple Level)**: This straightforward method shifts characters in the text by a fixed number of positions. However, it has a significant limitation—it can be easily **[bruteforced]((https://en.wikipedia.org/wiki/Brute-force_attack))** due to its single key and limited number of possible shifts.
  

- **Customized Encryption (On Normal level)**: To address the shortcomings of the Caesar cipher, a more advanced approach involves using multiple keys—a numerical key and a string key. This greatly reduces the likelihood of successful brute-force attacks.

- **Unicode-Compatible Encryption (On Advanced level)**: The most advanced method extends the concept to handle Unicode characters, which include a vast range of symbols beyond the basic alphabet. This approach enhances security significantly by using multiple keys and accommodating a much larger set of characters, making it highly resistant to brute-force attacks.

These algorithms demonstrates various ways to safeguard text using encryption keys. Understanding these techniques lays a strong foundation for further exploration into data security and privacy.

**©️ Ivin Techz 2024** 
