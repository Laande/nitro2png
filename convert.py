import sys
import zlib
from g_python.hpacket import HPacket


def convert(file):
    with open(file, 'rb') as f:
        data = f.read()

    packet = HPacket(0)
    packet.append_bytes(data)
    file_count = packet.read_short()

    for _ in range(file_count):
        name = packet.read_string()
        length = packet.read_int()
        compressed = packet.read_bytes(length)
        decompressed = zlib.decompress(compressed)
        
        yield name, decompressed

def save(file, r):
    with open(file, "wb") as f:
        f.write(r)
    
    
def main():
    if not sys.argv[1:]:
        print("Usage: python convert.py <file> [output]")
        exit(1)
        
    file = sys.argv[1]
    
    for name, data in convert(file):
        save(name, data)

    
if __name__ == "__main__":
    main()