numMap = {
          '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
          'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19,
          'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r': 27, 's': 28, 't': 29,
          'u': 30, 'v': 31, 'w': 32, 'x': 33, 'y': 34, 'z': 35
          }

# Returns 1 if input is valid, -1 otherwise
def checkInput(num, inBase, outBase):
    try:
        inBase = int(inBase)
        outBase = int(outBase)
    except ValueError:
        return -1

    for i in range(len(num)):
        if numMap[num[i]] > inBase:
            return -1
    if inBase < 2 or inBase > 36:
        return -1
    if outBase < 2 or outBase > 36:
        return -1

    return 1
