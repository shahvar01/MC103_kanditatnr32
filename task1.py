# Caesar Cipher Hacker
# Based on the brute-force Caesar method from:
# https://www.nostarch.com/crackingcodes/

def hack_caesar(message, SYMBOLS):
    for key in range(len(SYMBOLS)):
        translated = ''

        for symbol in message:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key

                if translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)

                translated = translated + SYMBOLS[translatedIndex]
            else:
                translated = translated + symbol

        print('Key #%s: %s' % (key, translated))


print("TEXT 1")
message = 'IJKLE LWPZQ LRTCW QFWWZ QDZFY OLYOQ FCJDT RYTQJ TYRYZ ESTYR'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
hack_caesar(message, SYMBOLS)

print("\nTEXT 2")
message = 'QBBJXUMEHBTYIQIJQWUQDTQBBJXUCUDQDTMECUDCUHUBOFBQOUHI'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
hack_caesar(message, SYMBOLS)

print("\nTEXT 3")
message = 'ZA z9 TcVmVi A5 3zE kyz4x9 r SzA sF vE6r4uz4x R26yrsvA r4u ruuz4x 4B3sv89'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
hack_caesar(message, SYMBOLS)