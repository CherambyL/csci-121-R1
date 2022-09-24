# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import string

alphabet = string.printable
ordinal_value = {ch: i for i, ch in enumerate(alphabet)}


def encrypt(message, key):
    encrypted_message = ''
    password = math. ceil(len(message) / len(password)) * password
    for index, ch in enumerate(message):
        pass_ch = password [index]
        key = ordinal_value [pass_ch]
        ord.of.ch = ordinal_value[ch]
        shifted_ord_of_ch = (ord_of_ch + key) % len(alphabet)
        encrypted_ch = alphabet [shifted_ord_of_ch]
        encrypted_message += encrypted_ch
    return encrypted_message

def decrypt (message, password):
    decrypted_message = ''
    password = math.ceil(Len(message) / Len(password)) * password
    for index, ch in enumerate(message):
        pass_ch = password [index]
        key = ordinal_value[pass_ch]
        ord.of.ch = ordinal_value[ch]
        shifted_ord_of_ch = (ord_of_ch - key) % len (alphabet)
        encrypted.ch = alphabet [shifted_ord_of_ch]
        encrypted_message += encrypted_ch
    return decrypted_message