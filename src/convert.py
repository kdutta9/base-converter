numMap = {
          '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
          'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19,
          'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r': 27, 's': 28, 't': 29,
          'u': 30, 'v': 31, 'w': 32, 'x': 33, 'y': 34, 'z': 35
          }
alphaCodes = {
            '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F',
            '16': 'G', '17': 'H', '18': 'I', '19': 'J', '20': 'K', '21': 'L',
            '22': 'M', '23': 'N', '24': 'O', '25': 'P', '26': 'Q', '27': 'R',
            '28': 'S', '29': 'T', '30': 'U', '31': 'V', '32': 'W', '33': 'X',
            '34': 'Y', '35': 'Z'
            }


# input is string, inBase and outBase are int types.
# outputs a string
def changeBase(input, inBase, outBase):
    decRep = convertToDec(input, inBase)
    if outBase == 10:
        return str(decRep)
    return convertToBase(decRep, outBase)


# takes input string and int inBase, outputs int type of base-10
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


# takes int types decRep and outBase, outputs string with base-outBase
def convertToBase(decRep, outBase):
    res = ''
    while decRep > 0:
        pop = decRep % outBase
        if pop >= 10:
            encoder = alphaCodes[str(pop)]
        else:
            encoder = str(pop)
        res = encoder + res
        decRep //= outBase
    return res
