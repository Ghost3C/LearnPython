#第一种使用maketrans,根据两个key一一对应替换加密字符串
import base64
STANDARD_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
CUSTOM_ALPHABET = 'WXYZlabcd3fghijko12e456789ABCDEFGHIJKL+/MNOPQRSTUVmn0pqrstuvwxyz'
EncodeStr = 'e6LJC+xnBq90daDNB+1TDrhG6aWG6p9LC/iNBqsGi2sVgJdqhZXDZoMMomKGoqxUE73N9qH\
0dZltjZ4RhJWUh2XiA6imBriT9/oGoqxmCYsiYG0fonNC1bxJD6pLB/1ndbaS9YXe9710A6t/CpVl963p9qDLC\
LViE2XlBqipB65SDciC4c3H8r1N8qaQdlpHBcDHC+4Go6tHBcLnA7hGebaICpVYA6tHC/LZBqVQ96i0A6xS7li\
M87X0973Fhe1hkG=='
DECODE_TRANS = str.maketrans(CUSTOM_ALPHABET, STANDARD_ALPHABET)

def decode(input):
    a = input.translate(DECODE_TRANS)
    return base64.b64decode(a)

print(decode(EncodeStr))
'''
#第二种使用for循环替换
import base64

STANDARD_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
CUSTOM_ALPHABET = 'WXYZlabcd3fghijko12e456789ABCDEFGHIJKL+/MNOPQRSTUVmn0pqrstuvwxyz'
EncodeStr = 'e6LJC+xnBq90daDNB+1TDrhG6aWG6p9LC/iNBqsGi2sVgJdqhZXDZoMMomKGoqxUE73N9qH\
0dZltjZ4RhJWUh2XiA6imBriT9/oGoqxmCYsiYG0fonNC1bxJD6pLB/1ndbaS9YXe9710A6t/CpVl963p9qDLC\
LViE2XlBqipB65SDciC4c3H8r1N8qaQdlpHBcDHC+4Go6tHBcLnA7hGebaICpVYA6tHC/LZBqVQ96i0A6xS7li\
M87X0973Fhe1hkG=='
#DECODE_TRANS = str.maketrans(CUSTOM_ALPHABET, STANDARD_ALPHABET)

s=""
for ch in EncodeStr:
    if(ch in  CUSTOM_ALPHABET):
        s+=STANDARD_ALPHABET[str.find(CUSTOM_ALPHABET,str(ch))] 
    elif (ch =='='):
        s+='='
x = base64.standard_b64decode(s)
print(x)
'''



