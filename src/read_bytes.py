# https://github.com/sirjonasxx/G-Python/blob/main/g_python/hpacket.py

class ReadBytes:
    def __init__(self, bytes):
        self.read_index = 0
        self.bytearray = bytearray(bytes)

    def read_int(self) -> int:
        r_int = int.from_bytes(self.bytearray[self.read_index:self.read_index + 4], byteorder='big', signed=True)
        
        self.read_index += 4
        return r_int

    def read_short(self) -> int:
        r_short = int.from_bytes(self.bytearray[self.read_index:self.read_index + 2], byteorder='big', signed=True)
        
        self.read_index += 2
        return r_short

    def read_string(self) -> str:
        encoding = 'iso-8859-1'
        
        len = self.read_short()
        r_string = self.bytearray[self.read_index:self.read_index + len].decode(encoding)
        
        self.read_index += len
        return r_string

    def read_bytes(self, len) -> bytearray:
        r_bytes = self.bytearray[self.read_index:self.read_index + len]
        
        self.read_index += len
        return r_bytes