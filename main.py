
morse_code = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    " ": "/"
}


# converts message to morse code
def translate_message():
    for x in message:
        print(morse_code[x])


# converts morse code to message
def translate_morse():
    arr = message.split(" ")
    for x in arr:
        print(list(morse_code.keys())[list(morse_code.values()).index(x)])


message = input("Enter message: ").upper()
if "-" and "." not in message:
    translate_message()
else:
    translate_morse()

