# cipher_breaker.py
# Educational implementation of Caesar and Vigenère ciphers, decryption, and cryptanalysis helper.
#
# Cryptographic Weaknesses:
# 1. Caesar Cipher:
#    - Monoalphabetic substitution.
#    - Extremely small keyspace (26 possible keys for English alphabet).
#    - Trivial to brute-force by shifting the ciphertext through all 26 keys.
# 2. Vigenère Cipher:
#    - Polyalphabetic substitution.
#    - Vulnerable to Kasiski examination (finding repeating sequences to determine key length).
#    - Vulnerable to Index of Coincidence (IC) analysis to identify key length.
#    - Once the key length L is determined, the ciphertext can be split into L Caesar ciphers
#      and solved using frequency analysis because letter distributions still leak information.

import sys

def caesar_encrypt(text: str, shift: int) -> str:
    """Encrypts text using the Caesar cipher with the given shift."""
    result = []
    shift = shift % 26
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result.append(chr(start + (ord(char) - start + shift) % 26))
        else:
            result.append(char)
    return "".join(result)

def caesar_decrypt(text: str, shift: int) -> str:
    """Decrypts text using the Caesar cipher with the given shift."""
    return caesar_encrypt(text, -shift)

def caesar_brute_force(ciphertext: str):
    """Prints all 26 possible decryptions of the Caesar cipher."""
    print("\n--- Caesar Brute-Force Results ---")
    for shift in range(26):
        decrypted = caesar_decrypt(ciphertext, shift)
        print(f"Shift {shift:02d}: {decrypted}")
    print("----------------------------------")

def vigenere_encrypt(text: str, key: str) -> str:
    """Encrypts text using the Vigenère cipher with the given key."""
    if not key.isalpha():
        raise ValueError("Key must contain alphabetic characters only.")
    
    result = []
    key = key.upper()
    key_idx = 0
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_idx % len(key)]) - ord('A')
            result.append(chr(start + (ord(char) - start + shift) % 26))
            key_idx += 1
        else:
            result.append(char)
    return "".join(result)

def vigenere_decrypt(text: str, key: str) -> str:
    """Decrypts text using the Vigenère cipher with the given key."""
    if not key.isalpha():
        raise ValueError("Key must contain alphabetic characters only.")
    
    result = []
    key = key.upper()
    key_idx = 0
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_idx % len(key)]) - ord('A')
            result.append(chr(start + (ord(char) - start - shift) % 26))
            key_idx += 1
        else:
            result.append(char)
    return "".join(result)

def main():
    while True:
        print("\n=== Classic Cipher Tool ===")
        print("1. Caesar Encrypt")
        print("2. Caesar Decrypt")
        print("3. Caesar Brute-Force Break")
        print("4. Vigenère Encrypt")
        print("5. Vigenère Decrypt")
        print("6. Exit")
        
        try:
            choice = input("Select an option (1-6): ").strip()
            if choice == '6':
                print("Exiting.")
                break
                
            if choice in ('1', '2'):
                text = input("Enter text: ")
                shift_str = input("Enter shift (integer 0-25): ").strip()
                if not shift_str.isdigit():
                    print("Error: Shift must be an integer.")
                    continue
                shift = int(shift_str)
                if choice == '1':
                    print("Result:", caesar_encrypt(text, shift))
                else:
                    print("Result:", caesar_decrypt(text, shift))
                    
            elif choice == '3':
                ciphertext = input("Enter Caesar ciphertext to brute-force: ")
                caesar_brute_force(ciphertext)
                
            elif choice in ('4', '5'):
                text = input("Enter text: ")
                key = input("Enter alphabetic key: ").strip()
                if not key.isalpha():
                    print("Error: Key must contain only letters.")
                    continue
                if choice == '4':
                    print("Result:", vigenere_encrypt(text, key))
                else:
                    print("Result:", vigenere_decrypt(text, key))
            else:
                print("Invalid selection.")
        except KeyboardInterrupt:
            print("\nExiting.")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
