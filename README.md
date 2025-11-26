# 🔏 Caesar & Vigenère Cipher Breaker (`cipher_breaker.py`)

## 💡 What is it?
This tool is an interactive cryptographic suite that encrypts, decrypts, and brute-force cracks messages encoded with classic substitution ciphers.

---

## 🚪 The Analogy
Imagine a secret decoder ring where you shift the outer wheel to align letters. If the shift key is 3, A becomes D, B becomes E, and so on. A **Caesar Cipher Breaker** is like a robot that turns the wheel to all 26 possible positions, prints the resulting message for each, and lets you quickly look to see which position reveals the readable secret message.

---

## ⚙️ How it Works
1. **Caesar Cipher (Monoalphabetic)**: Shists every letter in the plaintext by a single number (0 to 25).
2. **Vigenère Cipher (Polyalphabetic)**: Shifts letters using a keyword (e.g., "SECRET"). Each letter of the keyword determines a different shift value for corresponding letters of the message.
3. **Brute Force (Caesar)**: Since there are only 26 letters in the alphabet, there are only 26 possible keys. The script loops through all 26 options, decrypts the ciphertext for each shift, and displays them as a list. One of the options will read as plain English.

---

## 🛠️ Code Breakdown

* `ord(char)` & `chr(num)`: Converts characters to their ASCII numbers and back, allowing the script to perform basic math (addition/subtraction) for shifts.
* `(ord(char) - start + shift) % 26 + start`: Shifts the character within the bounds of uppercase (65-90) or lowercase (97-122) English letters.
* **Why Substitution Ciphers are Weak (Security Tip)**: These ciphers do not change the frequency of letters. In English, 'E' and 'T' are the most common letters. By analyzing letter frequencies, eavesdroppers can easily deduce the key.

---

## 🚀 How to Run
Run the script to launch the interactive menu:
```bash
python cipher_breaker.py
```
Choose from the options to encrypt, decrypt, or brute-force crack text.
