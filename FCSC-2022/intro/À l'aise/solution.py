from string import ascii_uppercase, ascii_lowercase

def vigenere_encrypt(message, key):
    """
    Vigenere encryption: (message + key) % 26
    """
    encrypted_message = ""
    key_index = 0

    for c in message:
        if c in ascii_lowercase:
            if key[key_index] in ascii_lowercase:
                encrypted_message += ascii_lowercase[(ascii_lowercase.index(c) + ascii_lowercase.index(key[key_index])) % 26]
            else:
                encrypted_message += ascii_lowercase[(ascii_lowercase.index(c) + ascii_uppercase.index(key[key_index])) % 26]

            key_index = (key_index + 1) % len(key)

        elif c in ascii_uppercase:
            if key[key_index] in ascii_lowercase:
                encrypted_message += ascii_uppercase[(ascii_uppercase.index(c) + ascii_lowercase.index(key[key_index])) % 26]
            else:
                encrypted_message += ascii_uppercase[(ascii_uppercase.index(c) + ascii_uppercase.index(key[key_index])) % 26]

            key_index = (key_index + 1) % len(key)
            
        else:
            encrypted_message += c

    return encrypted_message


def vigenere_decrypt(message, key):
    """
    Vigenere decryption: (message - key + 26) % 26
    """
    decrypted_message = ""
    key_index = 0

    for c in message:
        if c in ascii_lowercase:
            if key[key_index] in ascii_lowercase:
                decrypted_message += ascii_lowercase[(ascii_lowercase.index(c) - ascii_lowercase.index(key[key_index]) + 26) % 26]
            else:
                decrypted_message += ascii_lowercase[(ascii_lowercase.index(c) - ascii_uppercase.index(key[key_index]) + 26) % 26]

            key_index = (key_index + 1) % len(key)

        elif c in ascii_uppercase:
            if key[key_index] in ascii_lowercase:
                decrypted_message += ascii_uppercase[(ascii_uppercase.index(c) - ascii_lowercase.index(key[key_index]) + 26) % 26]
            else:
                decrypted_message += ascii_uppercase[(ascii_uppercase.index(c) - ascii_uppercase.index(key[key_index]) + 26) % 26]

            key_index = (key_index + 1) % len(key)

        else:
            decrypted_message += c

    return decrypted_message

message = "Gqfltwj emgj clgfv ! Aqltj rjqhjsksg ekxuaqs, ua xtwk n'feuguvwb gkwp xwj, ujts f'npxkqvjgw nw tjuwcz ugwygjtfkf qz uw efezg sqk gspwonu. Jgsfwb-aqmu f Pspygk nj 29 cntnn hqzt dg igtwy fw xtvjg rkkunqf."

key = "FCSC"

flag = vigenere_decrypt(message, key)
print(flag)