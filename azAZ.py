'''
Joon Bang
azAZ Task
INPUT: KLSadd.tex
OUTPUT: b.out
Converts a-z to A-Z, vice versa.
'''

FILE = 'KLSadd.tex'

f = open(FILE, 'r')
g = open('b.out', 'w')

text = f.read()
out = ''

for c in text:
    if ord(c) in range(65, 91): #if uppercase
        out += c.lower()
    elif ord(c) in range(97, 123): #if lowercase
        out += c.upper()
    else:
        out += c

g.write(out)

f.close()
g.close()
