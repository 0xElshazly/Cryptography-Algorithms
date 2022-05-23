# Vigenere Algorithm
# -------------------------------------------------
# Generate Key Function
def generateKey(text, key):
    if len(text) == len(key):
        return key
    elif len(text) < len(key):
        key = key[:len(text)]
        return key
    elif len(text) > len(key):
        for i in range(len(text) - len(key)):
            key += key[i % len(key)]
        return key
# -------------------------------------------------
# Encryption Function
alphabetCharacter = "abcdefghijklmnopqrstuvwxyz"
def encryption(plainText, key):
    cipherText = ""
    for i in range(len(plainText)):
        key = generateKey(plainText, key)
        print("Generated key is: " + key)
        for i in range(len(plainText)):
            p_value = alphabetCharacter.index(plainText[i])
            k_value = alphabetCharacter.index(key[i])
            c_value = (p_value + k_value) % 26
            c_char = alphabetCharacter[c_value]
            cipherText += c_char
        return cipherText
# -------------------------------------------------
# Decryption Function
def decryption(plainText, key):
    cipherText = ""
    for i in range(len(plainText)):
        key = generateKey(plainText, key)
        print("Generated key is: " + key)
        for i in range(len(plainText)):
            p_value = alphabetCharacter.index(plainText[i])
            k_value = alphabetCharacter.index(key[i])
            c_value = (p_value - k_value) % 26
            c_char = alphabetCharacter[c_value]
            cipherText += c_char
        return cipherText
# -------------------------------------------------
# Main Function
plainText = str.lower(input("Enter your plain text: "))
keyPlain = input("Enter your key: ")
print("Vigenere Cipher Text is: ", encryption(plainText, keyPlain))
print("-----------------------------------------")
cipherText = str.lower(input("Enter your cipher text: "))
keyCipher = input("Enter your key: ")
print("Plain Text is: ", decryption(cipherText, keyCipher))
# -------------------------------------------------