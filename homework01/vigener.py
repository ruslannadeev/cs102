def encrypt(plaintext, key):
    difference = len(plaintext) // len(key)
    key *= difference + 1
    ciphertext = ''
    for index, letter in enumerate(plaintext):
        replaced = (ord(letter) + ord(key[index]))
        encrypted  = chr(replaced % 26 + 65)
        ciphertext += encrypted
    return(ciphertext)

def decrypt(ciphertext, key):
    difference = len(ciphertext) // len(key)
    key *= difference + 1
    plaintext = ''
    for index, letter in enumerate(ciphertext):
        replaced_back = (ord(letter) - ord(key[index]))
        decrypted = chr(replaced_back % 26 + ord('A'))
        plaintext += decrypted
    return(plaintext)

plaintext = input('Enter a message: ').upper()
key = input('Enter a key : ').upper()
encrypted_msg = encrypt(plaintext, key)
decrypted_msg = decrypt(encrypted_msg, key)
print(encrypted_msg)
print(decrypted_msg)