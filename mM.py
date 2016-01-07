'''
Joon Bang
mM Task
INPUT: *.tex
OUTPUT: a.out
Converts M to m and vice versa.
'''


FILE = "KLSadd.tex"

f = open(FILE, "r")
g = open("a.out", "w")

text = f.read()
out = ''

for c in text:
    if c == 'm':
        out += 'M'
    elif c == 'M':
        out += 'm'
    else:
        out += c

g.write(out)

f.close()
g.close()
