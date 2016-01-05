'''
caseConvert - by Joon Bang
Input: FILE
Output: FILE.cnv

Switches cases of alphabet characters.

'''

import sys

def mM(FILE): #converts m's
    out = ''
    
    for c in open(FILE, 'r').read():
        if c == 'm':
            out += 'M'
        elif c == 'M':
            out += 'm'
        else:
            out += c
    
    f = open(FILE+'.cnv', 'w')
    f.write(out)
    f.close()

def azAZ(FILE): #converts all alphabet characters
    out = ''

    for c in open(FILE, 'r').read():
        if ord(c) in range(65, 91): #if uppercase
            out += c.lower()
        elif ord(c) in range(97, 123): #if lowercase
            out += c.upper()
        else:
            out += c
    
    f = open(FILE+'.cnv', 'w')
    f.write(out)
    f.close()
    
def usage(): #prints out usage
    print("Usage: caseConvert.py filename operation\n\toperation: m/azAZ")
    sys.exit(0)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage()
    else:
        if sys.argv[2] == "m":
            mM(sys.argv[1])
        elif sys.argv[2] == "az":
            azAZ(sys.argv[1])
        else:
            usage()