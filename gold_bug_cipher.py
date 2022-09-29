from re import X
import string
from tkinter import FALSE

alphabet = list(string.ascii_uppercase)
gold_bug_str = "5 2 - † 8 1 3 4 6 J K 0 9 * ‡ . Q ( ) ; ? ¶ W X : Z"
gold_bug_ls = list(gold_bug_str.split(" "))
gold_bug_str_join = "".join(gold_bug_ls)


def encrypt(rotor, plaintext):
    rotor = rotor.upper()
    rotor = [*rotor]
    plaintext = plaintext.upper()
    plaintext = [*plaintext]
    ciphertext = []

    # For each letter in the plaintext, find its index in the stardard alphabet.
    # Using this index, locate the substitube letter in the cipher alphabet.

    # Reminder: Numbers and symbols won't be encoded and are kept intact.
    # They could be mistaken for encoded characters later when attempting to decode.

    for x in plaintext:
        # If element at current idex is not a letter, append it to the ciphertext
        if not x.isalpha():
            ciphertext.append(x)
        for y in alphabet:
            if x == y:
                position = alphabet.index(y)
                ciphertext.append(rotor[position])
    ciphertext = "".join(ciphertext)
    return ciphertext


def decrypt(rotor, ciphertext):
    rotor = rotor.upper()
    rotor = [*rotor]
    ciphertext = ciphertext.upper()
    ciphertext = [*ciphertext]
    plaintext = []

    # For each letter in the ciphertext, find its index in the cipher alphabet.
    # This index will locate the letter in the standard alphabet. For example,
    # an index of2 means the third letter of the alphabet, which is C.

    # When using the gold bug cipher to decipher, numbers and symbols in the cipher will
    # be deciphered, while other elements are kept intact.

    if rotor == gold_bug_ls:
        for x in ciphertext:
            if x not in gold_bug_ls:
                plaintext.append(x)

            for y in rotor:
                if x == y:
                    position = rotor.index(y)
                    plaintext.append(alphabet[position])

    # When using a shuffled alphabet key to decipher, only letters are decoded.
    # Any non-letter char will be kept intact in the result.
    if rotor != gold_bug_ls:
        for x in ciphertext:
            if not x.isalpha():
                plaintext.append(x)
            for y in rotor:
                if x == y:
                    position = rotor.index(y)
                    plaintext.append(alphabet[position])

    plaintext = "".join(plaintext)
    return plaintext


def unique_characters(st):
    st = sorted(st)
    for i in range(len(st) - 1):
        if st[i] == st[i + 1]:
            return False
    return True


def is_allowed(str):
    str = str.upper()
    ls = list(str)
    for x in ls:
        if x not in alphabet and x not in gold_bug_ls:
            return False
        return True
