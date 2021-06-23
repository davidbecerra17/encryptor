# EncryptHandler module

#Rnd lib
import random

# The original symbols represent the characters that can be entered by the user in the message.
# Los simbolos originales representan los caracteres que pueden ser ingresados por el usuario en el mensaje.
original_symbols = "abcdefghijklmnñopqrstuvwxyz0123456789 .?"

# The old symbols represent some characters in random form that will be scrambled and then exchanged for the original characters.
# Los viejos simbolos representan algunos caracteres  en forma aleatoria que seran revueltos y despues intercambiados por los caracteres originales.
old_symbols = "qazwsxedcrfvtgbyhnujmikolpñ=!\"#$%&/()|*+"

# Returns the encrypted message given an original message and password.
# Retorna el mensaje encriptado dado un mensaje original y una contraseña.
def encrypt(message,password):
    encrypted_message = ""
    os = original_symbols
    ns = new_symbols(password)
    for character in message:
        i = os.find(character)
        encrypted_message += ns[i]
    i = 0
    first_characters = ""
    last_characters = ""
    for character in encrypted_message:
        if i < 3:
            first_characters += character
        else:
            last_characters += character
        i += 1
    encrypted_message = last_characters + first_characters
    return encrypted_message    

# Returns the original message given the encrypted message and a password.
# Retorna el mensaje original dado el mensaje encriptado y una contraseña.
def decrypt(encrypted_message,password):
    os = original_symbols
    ns = new_symbols(password)
    decrypted_message = ""
    last_characters = ""
    first_characters = ""
    i = 0
    for character in encrypted_message:
        if i <= len(encrypted_message) - 4:
            last_characters += character
        else:
            first_characters += character
        i += 1
    encrypted_message = first_characters + last_characters
    for character in encrypted_message:
        i = ns.find(character)
        decrypted_message += os[i]
    return decrypted_message

# Returns a new set of symbols, shuffling  the old symbols, given the sum of the ascii values of the password. 
# Retorna un conjunto nuevo de simbolos, revolviendo los viejos simbolos, dada la suma de los valores ascii de la contraseña. 
def new_symbols(password):
    seed = sum([ord(c) for c in password])
    symbols = old_symbols
    symbol_list = list(symbols)
    random.Random(seed).shuffle(symbol_list)
    result = ''.join(symbol_list)
    return result