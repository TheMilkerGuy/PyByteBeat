import math
from random import random as rand

def div(a, b): return a // b if b else 0
def b_and(a, b): return int(a) & int(b)
def b_or(a, b): return int(a) | int(b)
def rs(a, b): return int(a) >> int(b)
def ls(a, b): return int(a) << int(b)
def pw(a, b): return a ** b

functions = {
    'acos':math.acos,'acosh':math.acosh,'asin':math.asin,'asinh':math.asinh,'atan':math.atan,'atan2':math.atan2,
    'atanh':math.atanh,'cbrt':math.cbrt,'ceil':math.ceil,'comb':math.comb,'copysign':math.copysign,'cos':math.cos,
    'cosh':math.cosh,'degrees':math.degrees,'dist':math.dist,'e':math.e,'erf':math.erf,'erfc':math.erfc,'exp':math.exp,
    'exp2':math.exp2,'expm1':math.expm1,'fabs':math.fabs,'factorial':math.factorial,'floor':math.floor,'fma':math.fma,
    'fmod':math.fmod,'frexp':math.frexp,'fsum':math.fsum,'gamma':math.gamma,'gcd':math.gcd,'hypot':math.hypot,
    'inf':math.inf,'isclose':math.isclose,'isfinite':math.isfinite,'isinf':math.isinf,'isnan':math.isnan,'isqrt':math.isqrt,
    'lcm':math.lcm,'ldexp':math.ldexp,'lgamma':math.lgamma,'log':math.log,'log10':math.log10,'log1p':math.log1p,'log2':math.log2,
    'modf':math.modf,'nan':math.nan,'nextafter':math.nextafter,'perm':math.perm,'pi':math.pi,'pow':math.pow,'prod':math.prod,
    'radians':math.radians,'remainder':math.remainder,'sin':math.sin,'sinh':math.sinh,'sqrt':math.sqrt,'sumprod':math.prod,
    'tan':math.tan,'tanh':math.tanh,'tau':math.tau,'trunc':math.trunc,'ulp':math.ulp,'abs':abs,'int':int,'round':round,
    '^':pw,'//':div,'/':div,'&':b_and,'|':b_or,'>>':rs,'<<':ls
}

def _parse(equation, t):
    equation = equation.replace('t', 'int(t)')
    equation = equation.replace('/', '//')
    equation = equation.replace('////', '//')
    try:
        local_vars = {'t': int(t)}
        local_vars.update(functions)
        return eval(equation, {"__builtins__": None}, local_vars)
    except Exception as e:
        print(e)
        return 0

def _buffer(eq, s, k=8000):
    buffer = bytearray()
    for t in range(1, int(k) * s):
        sample = abs(int(_parse(eq, t)))
        sample = sample % 256
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
