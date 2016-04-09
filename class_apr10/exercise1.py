CIPHER_ENCRYPT = {"A": "X", "B": "Y", "C": "Z", "D": "A", "E": "B", "F": "C", "G": "D", "H": "E", "I": "F", "J": "G",
                  "K": "H", "L": "I", "M": "J", "N": "K", "O": "L", "P": "M", "Q": "N", "R": "O", "S": "P", "T": "Q",
                  "U": "R", "V": "S", "W": "T", "X": "U", "Y": "V", "Z": "W"}

CIPHER_DECRYPT = {"X": "A", "Y": "B", "Z": "C", "A": "D", "B": "E", "C": "F", "D": "G", "E": "H", "F": "I", "G": "J",
                  "H": "K", "I": "L", "J": "M", "K": "N", "L": "O", "M": "P", "N": "Q", "O": "R", "P": "S", "Q": "T",
                  "R": "U", "S": "V", "T": "W", "U": "X", "V": "Y", "W": "Z"}


def encrypt(message):
    new_message = ''

    # loop through all characters in message

    # if a character is in CIPHER_ENCRYPT.keys() then we will encrypt it
        # look for the character in the CIPHER_ENCRYPT and add the value to new_message

    # if the character is not found in CIPHER_ENCRYPT
        # then just add the character to new_message

    return new_message


def decrypt(message):
    new_message = ''

    # loop through all characters in message

    # if a character is in CIPHER_DECRYPT.keys() then we will encrypt it
        # look for the character in the CIPHER_DECRYPT and add the value to new_message

    # if the character is not found in CIPHER_DECRYPT
        # then just add the character to new_message

    return new_message


if __name__ == '__main__':
    # using the input function get a message from the user, store in a variable called message

    # convert the message to uppercase using the message.upper() function

    # call the encrypt() function passing message as a parameter, store the result in a variable called encrypted

    # print the encrypted message

    # call the decrypt() function passing encrypted as a parameter, store the result in a variable called decrypted

    # print the decrypted message
