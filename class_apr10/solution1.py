CIPHER_ENCRYPT = {"A": "X", "B": "Y", "C": "Z", "D": "A", "E": "B", "F": "C", "G": "D", "H": "E", "I": "F", "J": "G",
                  "K": "H", "L": "I", "M": "J", "N": "K", "O": "L", "P": "M", "Q": "N", "R": "O", "S": "P", "T": "Q",
                  "U": "R", "V": "S", "W": "T", "X": "U", "Y": "V", "Z": "W"}

CIPHER_DECRYPT = {"X": "A", "Y": "B", "Z": "C", "A": "D", "B": "E", "C": "F", "D": "G", "E": "H", "F": "I", "G": "J",
                  "H": "K", "I": "L", "J": "M", "K": "N", "L": "O", "M": "P", "N": "Q", "O": "R", "P": "S", "Q": "T",
                  "R": "U", "S": "V", "T": "W", "U": "X", "V": "Y", "W": "Z"}


def encrypt(message):
    new_message = ''
    for c in message:
        if c in CIPHER_ENCRYPT.keys():
            new_message += CIPHER_ENCRYPT[c]
        else:
            new_message += c
    return new_message


def decrypt(message):
    new_message = ''
    for c in message:
        if c in CIPHER_DECRYPT.keys():
            new_message += CIPHER_DECRYPT[c]
        else:
            new_message += c
    return new_message


if __name__ == '__main__':
    message = input('message to encrypt: ')

    message = message.upper()
    print('message:', message)

    encrypted_message = encrypt(message)
    print('encrypted message:', encrypted_message)

    decrypted_message = decrypt(encrypted_message)
    print('decrypted message:', decrypted_message)