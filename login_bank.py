import os

#vector with all the characters that can be used in the cezar cipher
vet_cezar = (
    # numbers
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    #alphabet lowercase 
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
    'u', 'v', 'w', 'x', 'y', 'z',
    #alphabet uppercase
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
    'U', 'V', 'W', 'X', 'Y', 'Z',
    #special characters
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', 
    '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', 
    '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', 
    '}', '~',
)

#mapping 
char_to_index = {char: idx for idx, char in enumerate(vet_cezar)}
index_to_char = {idx: char for idx, char in enumerate(vet_cezar)}

#function to encrypt the password using the cezar cipher
def encrepter_cezar(password, login, app):
    
    #initialize the encrypted password
    encrypted_password = ''

    #using the length of the password as the key
    ceazer_key = len(password)

    #encrypt the password using the key
    for char in password:
        if char in char_to_index:
            idx = char_to_index[char]
            new_idx = (idx + ceazer_key) % len(vet_cezar)
            encrypted_password += index_to_char[new_idx]
        #if the character is not in the vector, it keeps the original character
        else:
            encrypted_password += char  

    #return the encrypted password
    return encrypted_password

#function to decrypt the password using the cezar cipher
def decripter_cezar(encrypted_password):
    
    #initialize the decrypted password
    decrypted_password = ''

    #using the length of the encrypted password as the key
    ceazer_key = len(encrypted_password)

    #decrypt the password using the key
    for char in encrypted_password:
        if char in char_to_index:
            idx = char_to_index[char]
            new_idx = (idx - ceazer_key) % len(vet_cezar)
            decrypted_password += index_to_char[new_idx]
        #if the character is not in the vector, it keeps the original character
        else:
            decrypted_password += char

    #return the decrypted password
    return decrypted_password

#function to check if the password is correct
#this password is used to decrypt the encrypted password by the application
def is_password_correct(entered_password):
    return entered_password == "@126Lucas."

