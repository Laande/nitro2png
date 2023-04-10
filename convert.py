import binascii
import re
import sys

regex = b"89504e470d0a1a0a0000000d49484452(.*)0000000049454e44ae426082"


def convert(file):
    with open(file, "rb") as f:
        hexdata = binascii.hexlify(f.read())

    result = re.finditer(regex, hexdata)
    for i in result:
        r = i.group().decode()

    return r


def save(file, r):
    with open(file, "wb") as f:
        f.write(bytes.fromhex(r))
    
    
def main():
    if not sys.argv[1:]:
        print("Usage: python convert.py <file> [output]")
        exit(1)
        
    file = sys.argv[1]
    output = sys.argv[2] if len(sys.argv) > 2 else file + ".png"
    
    result = convert(file)
    save(output, result)

    
if __name__ == "__main__":
    main()