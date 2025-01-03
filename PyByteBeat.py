from math import *
from random import random as rand

def div(a, b): return a // b if b else 0
def truediv(a, b): return a / b if b else 0
def b_and(a, b): return int(a) & int(b)
def b_or(a, b): return int(a) | int(b)
def rs(a, b): return int(a) >> int(b)
def ls(a, b): return int(a) << int(b)
def pw(a, b): return a ** b

def _buffer(eq, s, k=8000):
    buffer = bytearray()
    for t in range(int(k) * s):
        try:
            sample = abs(int(eval(eq, {'acos': acos,'acosh': acosh,'asin': asin,'asinh': asinh,'atan': atan,'atan2': atan2,
        'atanh': atanh,'cbrt': cbrt,'ceil': ceil,'comb': comb,'copysign': copysign,'cos': cos,
        'cosh': cosh,'degrees': degrees,'dist': dist,'e': 2.718281828459045,'erf': erf,'erfc': erfc,'exp': exp,
        'exp2': exp2,'expm1': expm1,'fabs': fabs,'factorial': factorial,'floor': floor,'fma': fma,
        'fmod': fmod,'frexp': frexp,'fsum': fsum,'gamma': gamma,'gcd': gcd,'hypot': hypot,'inf': inf,
        'isclose': isclose,'isfinite': isfinite,'isinf': isinf,'isnan': isnan,'isqrt': isqrt,
        'lcm': lcm,'ldexp': ldexp,'lgamma': lgamma,'log': log,'log10': log10,'log1p': log1p,'log2': log2,
        'modf': modf,'nan': nan,'nextafter': nextafter,'perm': perm,'pi': pi,'pow': pow,'prod': prod,
        'radians': radians,'remainder': remainder,'sin': sin,'sinh': sinh,
        'sqrt': sqrt,'sumprod': prod,'tan': tan,'tanh': tanh,'tau': tau,'trunc': trunc,'ulp': ulp,
        'abs': abs, 'int': int, 'round': round, '^': pw, 't': t,
        '//': div, '/': truediv, '&': b_and, '|': b_or, '>>': rs, '<<': ls, 'ramd': rand
        })))
            sample = sample % 256
        except Exception as e:
            print(f"Error evaluating equation at t={t}: {e}")
            sample = 0
        buffer.append(sample & 0xFF)
    return buffer

def _wav(f, buffer, s, k=8000):
    num_samples = s * k
    byte_rate = k * 1
    block_align = 1 
    bits_per_sample = 8 
    header = bytearray()
    header.extend(b'RIFF')
    header.extend((36 + len(buffer)).to_bytes(4, 'little')) 
    header.extend(b'WAVE')
    header.extend(b'fmt ')
    header.extend((16).to_bytes(4, 'little'))
    header.extend((1).to_bytes(2, 'little'))
    header.extend((1).to_bytes(2, 'little'))
    header.extend((k).to_bytes(4, 'little'))
    header.extend((byte_rate).to_bytes(4, 'little'))
    header.extend((block_align).to_bytes(2, 'little'))
    header.extend((bits_per_sample).to_bytes(2, 'little'))
    header.extend(b'data')
    header.extend((len(buffer)).to_bytes(4, 'little'))
    with open(f, 'wb') as f:
        f.write(header)
        f.write(buffer)

equation = ''
seconds = 10
buffer = _buffer(equation, seconds)
output_file = "output.wav"
_wav(output_file, buffer, seconds)
