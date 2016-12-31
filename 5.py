from hashlib import md5

#seed = 'abc' #Test data, expected output 18f47a30
seed = 'cxdnnyjw'
index = 0
password = []

def get_next_hash(seed, index):
    s = seed + str(index)
    return md5(s.encode('utf-8')).hexdigest()

while len(password) < 8:
    h = get_next_hash(seed, index)
    if h.startswith('00000'):
        password.append(h[5])
    index += 1

print(''.join(password))

