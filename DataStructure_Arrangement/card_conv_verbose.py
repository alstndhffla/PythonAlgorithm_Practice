# 10진수 정수값을 입력받아 2~36진수로 변환하여 출력

def card_conv(x: int, r: int) -> str:
    """정수 x를 r 진수로 변환한 뒤 그 수를 나타내는 문자열을 반환"""

    d = ''  # 변환 뒤 문자열
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = len(str(x))  # 변환하기 전의 자릿수

    print(f'{r:2} | {x:{n}d}')
    while x > 0:
        print('   +' + (n + 2) * '-')
        if x // r:
            print(f'{r:2} | {x // r:{n}d} … {x % r}')
        else:
            print(f'     {x // r:{n}d} … {x % r}')
        d += dchar[x % r]  # 해당하는 문자를 꺼내 결합
        x //= r

    return d[::-1]  # 역순으로 반환


if __name__ == '__main__':
    print('10진수를 n 진수로 변환')

    while True:
        while True:
            no = int(input('음수가 아닌 양의 정수를 입력하세요:'))
            if no > 0:
                break

        while True:
            n = int(input('변환활 진수를 입력하세요(2~36진수 입력):'))
            if 2 <= n <= 36:
                break

        print(f"{no}를 {n}진수로 변환하면 {card_conv(no, n)}입니다.")

        retry = input("한번 더 할래? Y or N:")
        if retry in ['N', 'n']:
            break
