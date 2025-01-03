# PyByteBeat
Process your ByteBeat codes and output .wav files with Python (made by The Milker Guy because yes)

# How to use:
Paste the **PyByteBeat.py** source and make sure to put it right with your Python file.
Example of use (in your Python file):
```python
from PyByteBeat import *
equation = "((t >> 10) & 42) * t"
seconds = 5
buffer = _buffer(equation, seconds)
output_file = "output.wav"
_wav(output_file, buffer, seconds)
```

# Cautions
There are **NO** real PyPi modules of this so watch out for malicious modules! The only official source is this repository.

# Do I have to install any Pip libraries?
No, this script works without any Pip libraries but you surely need some Cowy love 😘.
