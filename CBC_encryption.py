def wordsToArray(words):
    array = []
    for word in words:
        for i in range(len(word)):
            array.append(word[i])
    return array


def intoBinaryNumber(number):
    binary_number = ''

    if (number != 0):
        while (number >= 1):
            if (number % 2 == 0):
                binary_number += '0'
                number = number / 2
            else:
                binary_number += '1'
                number = (number - 1) / 2

    while (len(binary_number) < 8):
        binary_number += '0'

    return ''.join(reversed(binary_number))


def arrayToBinary(array):
    binary_array = []
    for number in array:
        binary_array.append(intoBinaryNumber(number))
    return binary_array


def write(array):
    return(print(''.join([str(x) for x in array])))


def intoDecimalNumber(binary):
    decimal = 0
    for i in range(len(binary)):
        if (binary[i] == '1'):
            decimal += 2**i
    return decimal


def intoOpenText(array):
    text, j = '', 0
    translation = []
    for letter in array[::-1]:
        for let in letter[::-1]:
            text += let

    for i in range(7, len(text), 8):
        block = text[j:i + 1]
        letter = intoDecimalNumber(block)
        translation.append(chr(letter))
        j += 8
    return translation


def asciiValue(text):
    array = []
    for i in range(len(text)):
        array.append(ord(text[i]))
    return(array)


def xor(a, b):
    return str(int(a) ^ int(b))


def block_crypting(text, block_lenght):
    new = []
    for i in range(len(text)):
        if (i < block_lenght):
            new.append(xor(text[i], ini_vektor[i]))
        else:
            new.append(xor(text[i], text[i - block_lenght]))
            # stale je chyba tu, treba upravit text, nech neprichadza v poli abo co
    return new


## Cipher block chaning
text = input()
block_lenght = 8
ini_vektor = [0, 1, 1, 0, 1, 0, 1, 0]

text_in_binary = wordsToArray(arrayToBinary(asciiValue(text)))
crypted = block_crypting(text_in_binary, block_lenght)

write(text)
write(text_in_binary)
write(crypted)
write(intoOpenText(crypted))

