# Code below converts usual text to Morse code
morse_code = {
    "A" or "a": ".-",
    "B" or "b": "-...",
    "C" or "c": "-.-.",
    "D" or "d": "-..",
    "E" or "e": ".",
    "F" or "f": "..-.",
    "G" or "g": "--.",
    "H" or "h": "....",
    "I" or "i": "..",
    "J" or "j": ".---",
    "K" or "k": "-.-",
    "L" or "l": ".-..",
    "M" or "m": "--",
    "N" or "n": "-.",
    "O" or "o": "---",
    "P" or "p": ".--.",
    "Q" or "q": "--.-",
    "R" or "r": ".-.",
    "S" or "s": "...",
    "T" or "t": "-",
    "U" or "u": "..-",
    "V" or "v": "...-",
    "W" or "w": ".--",
    "X" or "x": "-..-",
    "Y" or "y": "-.--",
    "Z" or "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    " ": " / ",
    "!": "-.-.--",
    "?": "..--..",
    "'": ".----."
}

a = input(str("Write something: "))

for i in a.upper():
    for j in morse_code.keys():
        if i == j:
            print(morse_code.get(j), end=" ")
print("\nAll done")
