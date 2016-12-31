from hashlib import md5

#seed = 'abc' #Test data, expected output 18f47a30
seed = 'cxdnnyjw'
index = 0
password = [''] * 8

def get_next_hash(seed, index):
    s = seed + str(index)
    return md5(s.encode('utf-8')).hexdigest()

while '' in password:
    h = get_next_hash(seed, index)
    if h.startswith('00000'):
        i = int(h[5], 16)
        if i < 8 and  password[i] == '':
            password[i] = h[6]
    index += 1

print(''.join(password))

