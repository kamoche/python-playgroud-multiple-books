from struct import Struct

MyStruct = Struct('i?f')

data = MyStruct.pack(23, False, 42.0)

# All you get is a blob of data:
#>>> data
#b'x17x00x00x00x00x00x00x00x00x00(B'

# Data blobs can be unpacked again:
#>>> MyStruct.unpack(data)
#(23, False, 42.0)