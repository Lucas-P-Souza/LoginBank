import math
import os

def is_printable(char):
    return ord(char) >= 32 and ord(char) <= 126

def is_not_printable_up(char):
    id = ord(char)
    if id > 126:
        #i coded this way to make it easier to understand
        #if you want to make it more efficient, you can just do -> return id - 94
        id -= 126
        id += 32
    return id

def is_not_printable_down(char):
    id = ord(char)
    if id < 32:
        #i coded this way to make it easier to understand
        #if you want to make it more efficient, you can just do -> return id - 94
        id += 126
    return id

def encrepter_cezar():
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_filename = os.path.join(script_dir, 'output.txt')

    password = 'abc123.'
    ceazer_key_password = ''

    ceazer_key = len(password)

    for char in password:
        char = chr(ord(char) + ceazer_key)
        if is_printable(char):
            ceazer_key_password += char
        else:
            ceazer_key_password += chr(is_not_printable_up(char))

    new_password = ceazer_key_password

    with open(output_filename, 'w') as out_file:
        out_file.write(password + "\n")
        out_file.write(new_password + "\n")

def decripter_cezar():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_filename = os.path.join(script_dir, 'output.txt')

    with open(output_filename, 'r') as out_file:
        password = out_file.readline().strip()
        new_password = out_file.readline().strip()

    ceazer_key_password = ''

    ceazer_key = len(password)

    for char in new_password:
        char = chr(ord(char) - ceazer_key)
        if is_printable(char):
            ceazer_key_password += char
        else:
            ceazer_key_password += chr(is_not_printable_down(char))

    print(ceazer_key_password)
    
encrepter_cezar()
decripter_cezar()

'''
The code is not perfect, but it is a good start. You can improve it by adding more security layers, like using a better encryption algorithm, using a key to encrypt and decrypt, etc.
I hope this helps you. If you have any questions, please let me know.
'''
