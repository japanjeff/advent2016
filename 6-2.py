from collections import Counter

# Test data, yields "easter"
# lines = """eedadn
# drvtee
# eandsr
# raavrd
# atevrs
# tsrnev
# sdttsa
# rasrtv
# nssdts
# ntnada
# svetve
# tesnvt
# vntsnd
# vrdear
# dvrsen
# enarar""".split('\n')

with open('input-6.txt') as f:
    lines = f.readlines()

password = ''
for row in zip(*lines):
    common = Counter(row).most_common()[-1][0]
    password += common

print(password)
