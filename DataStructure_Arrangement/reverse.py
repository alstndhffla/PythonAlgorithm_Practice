# 뮤터블 시퀀스 원소를 역순으로 정렬
from typing import Any, MutableSequence


def reverse_array(a: MutableSequence) -> None:
    """뮤터블 시퀀스형 a의 원소를 역순으로 정렬"""
    n = len(a)
    # 가운데 값은 빼고 나머지는 앞 뒤 순서를 바꿔서 집어넣는다.
    for i in range(n // 2):
         a[i], a[n - i - 1] = a[n - i - 1], a[i]


if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬합니다.')
    nx = int(input('원소 수를 입력하세요.: '))
    x = [None] * nx   # 원소 수가 nx인 리스트를 생성

    # 원소 수 만큼 x 리스트에 추가.
    for i in range(nx):
        x[i] = int(input(f'x[{i}] : '))

    reverse_array(x)  # x를 역순으로 정렬

    print('배열 원소를 역순으로 정렬했습니다.')
    # 역순으로 정렬한 리스트의 원소 출력.
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')