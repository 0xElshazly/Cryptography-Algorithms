letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
keys =    ['q','w','e','r','t','y','u','i','o','p','a','s','d','m','g','h','j','k','l','z','x','c','v','b','n','f']
def encryption(text):
    cipher = []
    for l in text:
         key_number =  letters.index(l)
         new_letter = keys[key_number]
         cipher.append(new_letter)
    encrypt_text = ''.join(cipher)
    return encrypt_text

def decryption(text):
    cipher = []
    for l in text:
         letter_number =  keys.index(l)
         new_letter = letters[letter_number]
         cipher.append(new_letter)
    orginal_text = ''.join(cipher)
    return orginal_text

text  = str(input("Enter you Text >> ")).lower()
print("\nthe cipher text ==> " ,encryption(text))
print("\nthe plain text ==> ", decryption(text))