import zipfile
import zlib
from .read_bytes import ReadBytes


def convert(file):
    try:
        with zipfile.ZipFile(file, 'r') as zip_ref:
            for file_info in zip_ref.infolist():
                with zip_ref.open(file_info) as f:
                    data = f.read()
                    yield file_info.filename, data
    except zipfile.BadZipFile:
        with open(file, 'rb') as f:
            data = f.read()

        read_bytes = ReadBytes(data)
        file_count = read_bytes.read_short()

        for _ in range(file_count):
            decompressor = None
            name = read_bytes.read_string()
            length = read_bytes.read_int()
            compressed = read_bytes.read_bytes(length)
            if compressed.startswith(b'x\x9c'):
                decompressor = zlib.decompressobj()
            elif compressed.startswith(b'\x1f\x8b\x08'):
                decompressor = zlib.decompressobj(16 + zlib.MAX_WBITS)

            if decompressor:
                try:
                    decompressed = decompressor.decompress(compressed) + decompressor.flush()
                    yield name, decompressed
                except zlib.error as e:
                    print(f"Cant decompress the file {name}: {e}")
            else:
                print(f"Format unknown for {name}")


def save(file, r):
    with open(file, "wb") as f:
        f.write(r)
