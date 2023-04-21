import sys
import os
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
        decompressed = zlib.decompress(compressed)

        yield name, decompressed


def save(file, r):
    with open(file, "wb") as f:
        f.write(r)


def main():
    if not sys.argv[1:]:
        file_name = os.path.basename(__file__)
        print(f"Usage: python {file_name} <file> [output]")
        exit(1)

    file = sys.argv[1]

    for name, data in nitro2png(file):
        save(name, data)


if __name__ == "__main__":
    main()
