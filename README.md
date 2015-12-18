# Case Converter
By [Joon Bang](https://github.com/joonbang)

Converts uppercase letters to lowercase, and lowercase to uppercase.
# Installation
Download the Python file and drag-and-drop it into the same directory as files dependent on it.
# Methods
| Name | Return Type | Input |  Output  |                        Purpose                        |
|:----:|:-----------:|:-----:|:--------:|:-----------------------------------------------------:|
| mM   |     void    | FILE  | FILE.cnv | Switches the case of all m's in FILE.                 |
| azAZ |     void    | FILE  | FILE.cnv | Switches the case of all alphabet characters in FILE. |
# Usage
Import `caseConvert`.

Write any text that you want to convert into `FILE`.

Run the method you wish to use.

Read output from `FILE.cnv`.
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
