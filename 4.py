from collections import Counter, OrderedDict

# Test data
# lines = """aaaaa-bbb-z-y-x-123[abxyz]
# a-b-c-d-e-f-g-h-987[abcde]
# not-a-real-room-404[oarel]
# totally-real-room-200[decoy]""".split('\n')

with open('input-4.txt') as f:
    lines = f.readlines()

# We needed an ordered collections.Counter, found here:
# http://stackoverflow.com/a/35448557/
class OrderedCounter(Counter, OrderedDict):
    pass

def room_is_valid(letters, checksum):
    common = most_common_letters(letters)
    return checksum == ''.join(common)

def most_common_letters(letters):
    ordered = sorted(letters.replace('-',''))
    common = OrderedCounter(ordered).most_common()
    return [x[0] for x in common[0:5]]

def parse_checksum(line):
    begin = line.index('[') + 1
    end = line.index(']')
    return line[begin:end]

def parse_encrypted(line):
    end = line.index('[')
    data, _, sector = line[0:end].rpartition('-')
    return data, int(sector)

def rotate(letters, num):
    rotated = [rotate_letter(c, num) for c in letters]
    return ''.join(rotated)

def rotate_letter(c, num):
    if c == '-':
        return ' '
    ordinal = ord(c)-ord('a')
    rotated = (ordinal + num) % 26
    return chr(ord('a') + rotated)

sector_sum = 0
for line in lines:
    checksum = parse_checksum(line)
    letters, sector = parse_encrypted(line)
    if (room_is_valid(letters, checksum)):
        sector_sum += sector
        decoded = rotate(letters, sector)
        if 'north' in decoded:
            print(decoded, sector)

print(sector_sum)
