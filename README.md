# Cipher Wheel

## What it does
Cipher Wheel is a small terminal lab for Caesar and Vigenere ciphers. It encrypts, decrypts, and brute-forces classic substitution ciphers so you can see how old-school cryptography behaves in practice.

---

## How it works
1. **Caesar Cipher (Monoalphabetic)**: Shifts every letter in the plaintext by a single number (0 to 25).
2. **Vigenère Cipher (Polyalphabetic)**: Shifts letters using a keyword (e.g., "SECRET"). Each letter of the keyword determines a different shift value for corresponding letters of the message.
3. **Brute Force (Caesar)**: Since there are only 26 letters in the alphabet, there are only 26 possible keys. The script loops through all 26 options, decrypts the ciphertext for each shift, and displays them as a list. One of the options will read as plain English.

---

## Implementation notes

* `ord(char)` & `chr(num)`: Converts characters to their ASCII numbers and back, allowing the script to perform basic math (addition/subtraction) for shifts.
* `(ord(char) - start + shift) % 26 + start`: Shifts the character within the bounds of uppercase (65-90) or lowercase (97-122) English letters.
* **Why Substitution Ciphers are Weak (Security Tip)**: These ciphers do not change the frequency of letters. In English, 'E' and 'T' are the most common letters. By analyzing letter frequencies, eavesdroppers can easily deduce the key.

---

## Running it
Run the script to launch the interactive menu:
```bash
python cipher_breaker.py
```
Choose from the options to encrypt, decrypt, or brute-force crack text.


