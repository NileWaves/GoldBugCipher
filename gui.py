import PySimpleGUI as sg
from sub_cipher import *
import random

sg.theme("LightBrown2")
sample_text = """Jan 1 1864
I am John Jones who writes this letter. 
My ship is fast sinking with a treasure 
on board. I am where it is marked * on 
the enclosed chart."""

sample_text2 = """DECIPHER ME:
5 3‡‡† 305)) 6* ;48 26)4‡.') 4‡);80 
6* ;48 †8¶60') )85; 1‡(;:-‡*8 †83(88) 
5*† ;46(;88* 96*?;8) *‡(;485); 5*† 
2: *‡(;4 956* 2(5*-4 )8¶8*;4 0692 
85); )6†8 )4‡‡; 1(‡9 ;48 081; 8:8 ‡1 
;48 †85;4')-485† 5 288 06*8 1(‡9 ;48 
;(88 ;4(‡?34 ;48 )4‡; 161;: 188; ‡?;"""

layout = [
    [
        sg.Sizer(80, 2),
        sg.Text("Plain:  "),
        sg.Text("ABCDEFGHIJKLMNOPQRSTUVWXYZ", font="Courier 15"),
    ],
    [
        sg.Sizer(75, 2),
        sg.Button("Shuffle"),
        sg.Input(
            "DMTWSILRUYQNKFEJCAZBPGXOHV",
            font="Courier 15",
            key="-CIPHER-",
            size=(26, 1),
        ),
        sg.Text("", text_color=("red"), key="-ERROR-"),
    ],
    [sg.Sizer(70, 2), sg.Button("Gold-bug"), sg.Image()],
    [
        sg.Text("Plaintext:  "),
        sg.Multiline(sample_text, key="-INPUT-", size=(70, 15)),
        sg.Text("Ciphertext:  "),
        sg.Multiline(sample_text2, key="-INPUT2-", size=(70, 15)),
    ],
    [sg.Sizer(290, 2), sg.Ok("Encrypt"), sg.Sizer(540, 2), sg.Ok("Decrypt")],
    [
        sg.Text("Ciphertext: "),
        sg.Output(key="-OUTPUT-", size=(70, 15)),
        sg.Text("Plaintext:  "),
        sg.Output(key="-OUTPUT2-", size=(70, 15)),
    ],
]

window = sg.Window(
    "Gold Bug",
    layout,
    grab_anywhere=True,
    size=(1280, 720),
    icon="gold.ico",
)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "Gold-bug":
        window["-CIPHER-"].update(value=("".join(gold_bug_ls)))

    if event == "Shuffle":
        # create a new list of alphabet
        cipher = alphabet.copy()
        random.shuffle(cipher)
        # concactenate to a single string
        cipher = "".join(cipher)
        window["-CIPHER-"].update(value=cipher)

    if event == "Encrypt":
        rotor = values["-CIPHER-"]
        plaintext = values["-INPUT-"]

        # check if cipher alphabet contains 26* unique* letters*
        if len(rotor) != 26 or not unique_characters(rotor) or not is_allowed(rotor):
            error_msg = """Error: cipher alphabet must contain 26* unique* letters*,
            unless it is the gold-bug cipher."""
            window["-ERROR-"].update(value=error_msg)
            rotor = alphabet.copy()
            rotor = "".join(rotor)
        else:
            window["-ERROR-"].update(value="")
        # update the output box with encoded text
        ciphertext = encrypt(rotor, plaintext)
        window["-OUTPUT-"].update(value=ciphertext)

    if event == "Decrypt":
        rotor = values["-CIPHER-"]
        ciphertext = values["-INPUT2-"]

        if len(rotor) != 26 or not unique_characters(rotor) or not is_allowed(rotor):
            error_msg = """Error: cipher alphabet must contain 26* unique* letters*,
            unless it is the gold-bug cipher."""
            window["-ERROR-"].update(value=error_msg)
            rotor = alphabet.copy()
            rotor = "".join(rotor)
        else:
            window["-ERROR-"].update(value="")
        # update the output box with decoded text
        plaintext = decrypt(rotor, ciphertext)
        window["-OUTPUT2-"].update(value=plaintext)

window.close()
