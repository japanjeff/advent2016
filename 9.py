import itertools

with open('input-9.txt') as f:
    text = f.read().splitlines()[0]

# Test cases
#text = 'ADVENT' # Expected ADVENT
#text = 'A(1x5)BC' # Expected ABBBBBC
#text = '(3x3)XYZ' # Expected XYZXYZXYZ
#text = 'A(2x2)BCD(2x2)EFG' # Expected ABCBCEDFDFG
#text = '(6x1)(1x3)A' # Expected (1x3)A
#text = 'X(8x2)(3x3)ABCY' # Expected X(3x3)ABC(3x3)ABCY

decoded = ''

def CollectPlainText(iterable):
    return TakeUntilChar('(', iterable)

def Decode(iterable, chars, multiplier):
    charsToMultiply = list(itertools.islice(iterable, chars))
    toMultiply = ''.join(charsToMultiply)
    return toMultiply * multiplier

def GetDecodeParms(iterable):
    chars = TakeUntilChar('x', iterable)
    multiplier = TakeUntilChar(')', iterable)
    if not chars and not multiplier:
        return False, 0, 0

    return True, int(chars), int(multiplier)

def TakeUntilChar(char, iterable):
    collected = itertools.takewhile(lambda x: x != char, iterable)
    return ''.join(collected)

iterable = iter(text)
decoded += CollectPlainText(iterable)

while True:
    found, chars, multiplier = GetDecodeParms(iterable)
    if not found:
        break;

    decoded += Decode(iterable, chars, multiplier)
    morePlainText = CollectPlainText(iterable)
    decoded += morePlainText

print(len(decoded))
