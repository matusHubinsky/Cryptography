def xor(a, b):
    return str(int(a) ^ int(b))


def write(array):
    return(print(''.join([str(x) for x in array])))


def decrypt(text, block_lenght):
    new = []
    for i in range(len(text)):
        if i < block_lenght:
            new.append(str(xor(text[i], i_vector[i])))
        else:
            new.append(str(xor(text[i], new[i - block_lenght])))
    return new


def intoDecimalNumber(binary):
    decimal = 0
    for i in range(len(binary)):
        if (binary[i] == '1'):
            decimal += 2**i
    return decimal


def binaryToNumbers(translate):
    text = translate[::-1]
    j = 0
    translation = []
    for i in range(7, len(text), 8):
        blok = text[j:i + 1]
        word = int(intoDecimalNumber(blok))
        translation.append(chr(word))
        j += 8
    return translation


encypted = input()
block_lenght = 8
i_vector = [0, 1, 1, 0, 1, 0, 1, 0]
key = [0] * block_lenght

write(i_vector)
binary_text = decrypt(encypted, block_lenght)
write(binary_text)

text = binaryToNumbers(binary_text)
write(text[::-1])
