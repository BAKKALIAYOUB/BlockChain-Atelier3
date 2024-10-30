import struct
import math

class MD5:
    # Constants for MD5
    s = [
        7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
        5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
        4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
        6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21,
    ]
    
    K = [
        int(abs(math.sin(i + 1)) * (2 ** 32)) & 0xFFFFFFFF for i in range(64)
    ]
    

    def __init__(self, message):
        self.message = message

    def left_rotate(self, x, amount):
        x &= 0xFFFFFFFF
        return ((x << amount) | (x >> (32 - amount))) & 0xFFFFFFFF

    def encode(self):
        # Step 1: Initialize variables
        A = 0x67452301
        B = 0xEFCDAB89
        C = 0x98BADCFE
        D = 0x10325476

        # Step 2: Pre-processing: Padding the message
        message = self.message
        original_byte_len = len(message)
        original_bit_len = original_byte_len * 8
        message += b'\x80'   # In Byte 10000000 = 0x80
        while len(message) % 64 != 56:
            # Padd the message until the size of the message in bits is 512 bits
            message += b'\x00' 
        message += struct.pack('<Q', original_bit_len)

        # Step 3: Process the message in 512-bit (64-byte) chunks
        for i in range(0, len(message), 64):
            a, b, c, d = A, B, C, D
            chunk = message[i:i+64]
            M = struct.unpack('<' + 'I' * 16, chunk)

            # Main loop:
            for j in range(64):
                if 0 <= j <= 15:
                    f = (b & c) | (~b & d)
                    g = j
                elif 16 <= j <= 31:
                    f = (d & b) | (~d & c)
                    g = (5 * j + 1) % 16
                elif 32 <= j <= 47:
                    f = b ^ c ^ d
                    g = (3 * j + 5) % 16
                elif 48 <= j <= 63:
                    f = c ^ (b | ~d)
                    g = (7 * j) % 16

                f = (f + a + self.K[j] + M[g]) & 0xFFFFFFFF
                a, d, c, b = d, (b + self.left_rotate(f, self.s[j])) & 0xFFFFFFFF, b, c

            # Add this chunk's hash to result so far
            A = (A + a) & 0xFFFFFFFF
            B = (B + b) & 0xFFFFFFFF
            C = (C + c) & 0xFFFFFFFF
            D = (D + d) & 0xFFFFFFFF

        return '{:08x}{:08x}{:08x}{:08x}'.format(A, B, C, D)



# Example usage
if __name__ == "__main__":
    message = b"hello"
    md5_instance = MD5(message)
    print("MD5 hash:", md5_instance.encode())
    
