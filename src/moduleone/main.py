def caeser_cipher(message, shift, direction=1):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    final_message = ""

    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            char_index = alphabet.index(char)
            new_char_index = char_index + shift * direction
            final_message += alphabet[new_char_index % len(alphabet)]
    return final_message


def encrypt_caeser_cipher(message, shift):
    return caeser_cipher(message, shift)


def decrypt_caeser_cipher(encription, shift):
    return caeser_cipher(encryption, shift, -1)


world = "gabriel@antunes"
shift = 3
encryption = encrypt_caeser_cipher(world, shift)
print(f"Encryption: {encryption}")

decryption = decrypt_caeser_cipher(encryption, shift)
print(f"\nDecription: {decryption}")
