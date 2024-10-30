# MD5 Algorithm 

The MD5 (Message-Digest Algorithm 5) is a widely used cryptographic hash function that produces a 128-bit hash value from an input message. This Python implementation follows the steps outlined in the MD5 specification.

## Algorithm Steps

1. **Initialize Variables** : The algorithm starts by initializing four 32-bits variables (A, B, C, D) with the following hexadecimal values:
    * `A = 0x67452301`
    * `B = 0xEFCDAB89`
    * `C = 0x98BADCFE`
    * `D = 0x10325476`
2. **Pre-Processing** : Padding the Message: The input message is padded to ensure that its length is congruent to 448 modulo 512. This is done by appending a single `1` bit to the message, followed by as many `0`  bits until the length is 448 bits. Then, the original length of the message (in bits) is appended as 64-bits little-endian integer.
3. **Process The message in 512-bits chunks** : The padded message is divided into 512-bit (64-byte) chunks, and each chunk is processed as follows:
    * Copy the current values of A, B, C, and D into temporary variables a, b, c, and d, respectively.
    * Perform 64 rounds of a complex compression function that involves a combination of logical operations, additions, and left rotations. The compression function uses four rounds, each with 16 steps, defined by different formulas.
    * Update the values of A, B, C, and D by adding the temporary variables a, b, c, and d, respectively.
4. **Output** : After all the chunks have been processed, the final values of A, B, C, and D are concatenated to produce the 128-bit hash value, which is then represented as a 32-character hexadecimal string.


## Example Usage

```python
import md5
message = b"hello"
md5_instance = md5.MD5(message)
print("MD5 hash:", md5_instance.encode())
```