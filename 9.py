import itertools

def collect_plain_text(iterable):
    return take_until_char('(', iterable)

def decode(iterable, chars, multiplier):
    charsToMultiply = list(itertools.islice(iterable, chars))
    toMultiply = ''.join(charsToMultiply)
    return toMultiply * multiplier

def get_decode_parms(iterable):
    chars = take_until_char('x', iterable)
    multiplier = take_until_char(')', iterable)
    if not chars and not multiplier:
        return False, 0, 0

    return True, int(chars), int(multiplier)

def take_until_char(char, iterable):
    collected = itertools.takewhile(lambda x: x != char, iterable)
    return ''.join(collected)

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
iterable = iter(text)
decoded += collect_plain_text(iterable)

while True:
    found, chars, multiplier = get_decode_parms(iterable)
    if not found:
        break;

    decoded += decode(iterable, chars, multiplier)
    morePlainText = collect_plain_text(iterable)
    decoded += morePlainText

print(len(decoded))
