from re import X
import string
from tkinter import FALSE

alphabet = list(string.ascii_uppercase)
gold_bug_str = "5 2 - † 8 1 3 4 6 J K 0 9 * ‡ . Q ( ) ; ? ¶ W X : Z"
gold_bug_ls = list(gold_bug_str.split(" "))


def encrypt(rotor, plaintext):
    rotor = rotor.upper()
    rotor = [*rotor]
    plaintext = plaintext.upper()
    plaintext = [*plaintext]
    ciphertext = []

    # For each letter in the plaintext, find its index in the stardard alphabet.
    # Using this index, locate the substitube letter in the cipher alphabet.
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
    for x in ciphertext:
        if not is_allowed(x):
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


# check if a string contains char outside of the "alphabet" and "gold_bug_ls" lists.
def is_allowed(str):
    ls = list(str)
    for x in ls:
        if x not in alphabet and x not in gold_bug_ls:
            return False
    return True
