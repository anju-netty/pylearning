# Shebang #!

#!/usr/bin/python3 is a shebang line.

A shebang line defines where the interpreter is located. In this case, the python3 interpreter is located in /usr/bin/python3. A shebang line could also be a bash, ruby, perl or any other scripting languages' interpreter, for example: #!/bin/bash.

Without the shebang line, the operating system does not know it's a python script, even if you set the execution flag on the script and run it like ./script.py. To make the script run by default in python3, either invoke it as python3 script.py or set the shebang line.

You can use #!/usr/bin/env python3 for portability across different systems in case they have the language interpreter installed in different locations.

# How to locate the location of the python3 interpreter?

### First option:
sys.executable contains full path of the currently running Python interpreter.
```python
import sys
print(sys.executable)

Output:
/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
```
### Second option:
-----------------
```bash
$ which python
/usr/local/bin/python
$ which python3
/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
```
## CSV and CSV dialets 
(*Parameters defining delimiters and lineterminators*)

[tutorial](https://wellsr.com/python/introduction-to-csv-dialects-with-the-python-csv-module/)