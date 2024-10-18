alphabet = 26

def generate_vigenere_key(text, key):
    key = list(key)
    if len(key) < len(text):
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def vigenere_encrypt(text, key):
    encrypted_text = ""
    for i in range(len(text)):
        if text[i].isalpha():
            shift = (ord(text[i].lower()) - 97 + ord(key[i].lower()) - 97) % alphabet
            encrypted_text += chr(shift + 97)
        else:
            encrypted_text += text[i]
    return encrypted_text

def vigenere_decrypt(text, key):
    decrypted_text = ""
    for i in range(len(text)):
        if text[i].isalpha():
            shift = (ord(text[i].lower()) - ord(key[i].lower())) % alphabet
            decrypted_text += chr(shift + 97)
        else:
            decrypted_text += text[i]
    return decrypted_text


text = "explanation"
key = "leg"

generated_key = generate_vigenere_key(text, key)

encrypted_text = vigenere_encrypt(text, generated_key)
print(f"Encrypted Text: {encrypted_text}")

decrypted_text = vigenere_decrypt(encrypted_text, generated_key)
print(f"Decrypted Text: {decrypted_text}")