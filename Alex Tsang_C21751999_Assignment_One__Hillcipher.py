import numpy as np
from sympy import Matrix

alphabet = 26

def mod_inverse(a, m):
    # Calculate the modular inverse of a under modulo m using Extended Euclidean Algorithm
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def hill_encrypt(plaintext, key_matrix):
    plaintext = plaintext.lower().replace(" ", "")
    if len(plaintext) % 2 != 0:
        plaintext += 'x'  # Padding if the length is odd

    encrypted_text = ""
    for i in range(0, len(plaintext), 2):
        pair = [ord(plaintext[i]) - 97, ord(plaintext[i + 1]) - 97]
        encrypted_pair = np.dot(key_matrix, pair) % alphabet
        encrypted_text += chr(encrypted_pair[0] + 97) + chr(encrypted_pair[1] + 97)
    
    return encrypted_text

def hill_decrypt(ciphertext, key_matrix):
    ciphertext = ciphertext.lower().replace(" ", "")
    decrypted_text = ""

    # Calculate the inverse of the key matrix modulo 26
    key_matrix_inv = Matrix(key_matrix).inv_mod(alphabet)
    key_matrix_inv = np.array(key_matrix_inv).astype(int)

    for i in range(0, len(ciphertext), 2):
        pair = [ord(ciphertext[i]) - 97, ord(ciphertext[i + 1]) - 97]
        decrypted_pair = np.dot(key_matrix_inv, pair) % alphabet
        decrypted_text += chr(decrypted_pair[0] + 97) + chr(decrypted_pair[1] + 97)
    
    return decrypted_text


key_matrix = [[3, 6], [4, 7]]  
plaintext = "lemonade"


encrypted_text = hill_encrypt(plaintext, key_matrix)
print(f"Encrypted Text: {encrypted_text}")


decrypted_text = hill_decrypt(encrypted_text, key_matrix)
print(f"Decrypted Text: {decrypted_text}")