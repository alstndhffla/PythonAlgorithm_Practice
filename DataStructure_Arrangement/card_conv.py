# 10진수 정수값을 입력받아 2~36진수로 변화하여 출력

def card_conv(x: int, r: int) -> str:
    # 정수값 x 를 r 진수로 변환, 그리고 그 수를 나타내는 문자열을 반환.

    # 변환 후 문자열
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0:
        # x 를 r 로 나눈 나머지의 값 위치에 있는 문자를 d 에 결합.
        # 문자열 d의 맨 앞은 마지막으로 구한 문자가 된다.
        # 나눗셈의 나머지 %
        # print(f"x % r: {x % r}")
        d += dchar[x % r]
        # d = d + dchar[x % r]
        # print(f"d: {d}")

        # 나눗셈 후 몫을 반환 //
        # print(f"x//r: {x//r}")
        x //= r
        # x = x // r
        # print(f"x: {x}")

    # 리스트에 저장되어 있는 값을 거꾸로 변환해 반환하면 진수변환된 값을 만들 수 있다
    return d[::-1]


# print(card_conv(1234, 10))


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
