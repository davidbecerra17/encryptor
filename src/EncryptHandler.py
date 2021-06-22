import random

original_symbols = "abcdefghijklmnñopqrstuvwxyz0123456789 .?"
old_symbols = "qazwsxedcrfvtgbyhnujmikolpñ=!\"#$%&/()|*+"

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

def new_symbols(password):
    seed = avg([ord(c) for c in password])
    symbols = old_symbols
    symbol_list = list(symbols)
    random.Random(seed).shuffle(symbol_list)
    result = ''.join(symbol_list)
    return result

def avg(list):
    return int(sum(list) / len(list))