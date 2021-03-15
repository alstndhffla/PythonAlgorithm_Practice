# 10진수 정수값을 입력받아 2~36진수로 변화하여 출력

def card_conv(x: int, r: int) -> str:
    # 정수값 x 를 r 진수로 변환, 그리고 그 수를 나타내는 문자열을 반환.

    # 변환 후 문자열
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0:
        d += dchar[x % r]
        # d = d + dchar[x % r]
        x //= r
        # x = x // r

    return d[::-1]

