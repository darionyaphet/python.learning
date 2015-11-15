import binascii

'''convert between binary and various ASCII-encoded'''
encoding = binascii.b2a_hex('darion.yaphet')
print(encoding)
print(binascii.a2b_hex(encoding))

'''base64 maybe ok'''

import base64
encoding = base64.b16encode('darion.yaphet')
print(encoding)
print(base64.b16decode(encoding))
