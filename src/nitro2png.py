import zlib
from .read_bytes import ReadBytes


def nitro2png(file):
    with open(file, 'rb') as f:
        data = f.read()

    read_bytes = ReadBytes(data)
    file_count = read_bytes.read_short()

    for _ in range(file_count):
        name = read_bytes.read_string()
        length = read_bytes.read_int()
        compressed = read_bytes.read_bytes(length)
        if compressed.startswith(b'x\x9c'):
            decompressed = zlib.decompress(compressed)
        elif compressed.startswith(b'\x1f\x8b\x08'):
            decompressed = zlib.decompress(compressed, 16+zlib.MAX_WBITS)
        else:
            continue

        yield name, decompressed


def save(file, r):
    with open(file, "wb") as f:
        f.write(r)
