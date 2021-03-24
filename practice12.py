# 12.1
import unicodedata

mystery = '\U0001f4a9'

print(mystery)
print(unicodedata.name(mystery))

# 12.2
pop_bytes = mystery.encode('utf-8')

print(pop_bytes)

# 12.3
pop_string = pop_bytes.decode('utf-8')

print(pop_string)

print(mystery == pop_string)

# 12.4
mammoth = '''
    We have seen thee, queen of cheese,
    Lying quietly at your ease,
    Gently fanned by evening breeze,
    Thy fair form no flies dare seize.

    All gaily dressed soon you'll go
    To the great Provincial show,
    To be admired by many a beau
    In the city of Toronto.

    Cows numerous as a swarm of bees,
    Or as the leaves upon the trees,
    It did require to make thee please,
    And stand unrivalled, queen of cheese.

    May you not receive a scar as
    We have heard that Mr. Harris
    Intends to send you off as far as
    The great world's show at Paris.

    Of the youth beware of these,
    For some of them might rudely squeeze
    And bite your cheek, then songs or glees
    We could not sing, oh! queen of cheese.

    We'rt thou suspended from balloon,
    You'd cast a shade even at noon,
    Folks would think it was the moon
    About to fall and crush them soon.
    '''

# 12.5
import re

print(*re.findall(r'(?<= |\n)c\w*', mammoth))

# 12.6
print(*re.findall(r'(?<= |\n)c\w{3}(?=\W)', mammoth))

# 12.7
print(*re.findall(r'(?<= |\n)\w*r(?=\W)', mammoth))

# 12.8
print(*re.findall(r'(?<= |\n)\w*[aeiou]{3}\w*', mammoth))

# 12.9
import binascii
gif = binascii.unhexlify('47494638396101000100800000000000ffffff21f9' + \
                            '0401000000003c000000000100010000020144003b')

print(gif)

# 12.10
print(bool(re.match(b'GIF89a', gif)))

# 12.11
import struct

print(*struct.unpack('<HH', gif[6:10]))