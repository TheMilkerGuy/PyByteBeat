def _buffer(eq, s, k=8000):
    buffer = bytearray()
    for t in range(int(k) * s):
        sample = abs(int(eval(eq)))
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
