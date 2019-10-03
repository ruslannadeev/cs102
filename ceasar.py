def encrypt(plaintext, key):
    ciphertext = ''
    
    for letter in plaintext:
        replaced = ord(letter)+int(key)
        if (ord(letter) < 65 or 90 < ord(letter) < 97 or ord(letter) > 122):  
            ciphertext += letter
        elif replaced > 90 and letter.isupper()==True:
            while replaced > 90:
                replaced -= 26
            letter_encrypted = chr(replaced)
            ciphertext += letter_encrypted
        elif replaced > 122 and letter.islower()==True:
            while replaced > 122:
                replaced -= 26
            letter_encrypted = chr(replaced)
            ciphertext += letter_encrypted       
        else:
            letter_encrypted = chr(replaced)
            ciphertext += letter_encrypted
    return(ciphertext)

def decrypt(ciphertext, key):
    plaintext = ''
    
    for letter in ciphertext:
        replaced_back = ord(letter) - int(key)
        if (ord(letter) < 65 or 90 < ord(letter) < 97 or ord(letter) > 122):  
            plaintext += letter
        elif replaced_back < 65 and letter.isupper()==True:
            while replaced_back < 65:
                replaced_back += 26
            letter_decrypted = chr(replaced_back)
            plaintext += letter_decrypted
        elif replaced_back < 97 and letter.islower()==True:
            while replaced_back < 97:
                replaced_back += 26
            letter_decrypted = chr(replaced_back)
            plaintext += letter_decrypted       
        else:
            letter_decrypted = chr(replaced_back)
            plaintext += letter_decrypted
    return(plaintext)

plaintext = input('Enter a message: ')
key = input('Enter a key : ')
encrypted = encrypt(plaintext, key)
decrypted = decrypt(encrypted, key)
print(encrypted)
print(decrypted)