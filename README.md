# Case Converter
By [Joon Bang](https://github.com/joonbang)

Converts uppercase letters to lowercase, and lowercase to uppercase. Written in Python 3.x, but compatible with Python 2.x.

Case Converter reads from an input file, and writes to an output file; it *does not* modify the input file. When using Case Converter, make sure to specify the absolute file path to the input file.

# Installation
Download the Python file. If meant to used as a library, move it to the same directory of Python files dependent on it.

# Methods
| Name | Return Type | Input File |  Output File  |                        Purpose                        |
|:----:|:-----------:|:----------:|:-------------:|:-----------------------------------------------------:|
| mM   |     void    |    FILE    |   FILE.cnv    | Switches the case of all m's in FILE.                 |
| azAZ |     void    |    FILE    |   FILE.cnv    | Switches the case of all alphabet characters in FILE. |

# Usage
Case Converter can be called through the shell. It has two arguments, the file name and the letters to convert (m/az). 

Alternatively, it can be used as a stand-alone library in Python. To use in Python, import the module; the methods will then be usable. The methods have one argument/input, `FILE`, and write the output to `FILE.cnv`. 

### Sample Code
```
import caseConvert

sampleText = "Hello darkness my old friend..."

FILE = "sample1.txt"

with open(FILE, 'w') as f:
  f.write(sampleText)

caseConvert.azAZ(FILE)

with open(FILE, 'r') as f:
  print(f.read()) #output: "hELLO DARKNESS MY OLD FRIEND..."
```

# See also
[ASCII Table] (http://www.asciitable.com/)
