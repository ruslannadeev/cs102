def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """

    difference = len(plaintext) // len(keyword)
    keyword *= difference + 1
    ciphertext = ''
    for index, letter in enumerate(plaintext):
        replaced = (ord(letter) + ord(keyword[index]))
        encrypted = chr(replaced % 26 + 65)
        ciphertext += encrypted
    return(ciphertext)


def decrypt_vigenere(ciphertext, keyword):
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """

    difference = len(ciphertext) // len(keyword)
    keyword *= difference + 1
    plaintext = ''
    for index, letter in enumerate(ciphertext):
        replaced_back = (ord(letter) - ord(keyword[index]))
        decrypted = chr(replaced_back % 26 + ord('A'))
        plaintext += decrypted
    return(plaintext)
