'''
3.1.2.10 LAV: La declaración de continuación: el devorador de vocales feo
'''

def devorador():
    user_word = input("Ingrese la Palabra: ")
    user_word = user_word.upper()
    for letter in user_word:
        if letter == "A":
            continue
        elif letter == "E":
            continue
        elif letter == "I":
            continue
        elif letter == "O":
            continue
        elif letter == "U":
            continue
        else:
            print(letter)
devorador()