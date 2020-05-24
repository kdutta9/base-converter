numMap = {
          '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
          'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19,
          'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r': 27, 's': 28, 't': 29,
          'u': 30, 'v': 31, 'w': 32, 'x': 33, 'y': 34, 'z': 35
          }

def changeBase(input, inBase, outBase):
    decRep = convertToDec(input, inBase)
    if outBase == 10:
        return str(decRep)
    return convertToBase(decRep, outBase)


def convertToDec(input, inBase):
    if inBase == 10:
        return int(input)
    res = 0
    power = 0
    for i in range(-1, -1 * len(input) - 1, -1):
        digit = input[i]
        longForm = numMap[digit.lower()]

        place = (inBase ** power) * longForm
        power += 1
        res += place

    return res


def convertToBase(decRep, outBase):
    res = ''
    while decRep > 0:
        pop = decRep % outBase
        res = numMap[pop] + res
        decRep //= outBase
    return res
