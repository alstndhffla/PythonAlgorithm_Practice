# binary search
from typing import Any, Sequence


def bin_search(a: Sequence, key: Any) -> int:
    """
    시퀀스에서 a에서 key와 일치하는 원소를 이진검색
    """
    pl = 0
    pr = len(a-1)

    while True:
        pc = (pl+pr)//2
        if a[pc] == key:
            return pc
        elif a[pc] < key:   # 키값보다 중앙값이 작기 때문에 앞범위를 중앙값보다 한칸 크게 변화시킨다.
            pl = pc + 1
        else:               # 그 반대로 뒷범위를 중앙값보다 한칸 작게 변화시킨다.
            pr = pc - 1
        if pl > pr:         # 계속 범위를 줄이다가 각자의 범위가 어긋나면 멈춘다.
            break
        return -1           # 검색 실패


if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요:'))
    x = [None] * num

    print('배열 데이터를 오름차순으로 입력하세요.')

    x[0] = int(input('x[0]: '))     # 최초의 값을 입력하고

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]'))
            if x[i] >= x[i - 1]:
                break

    ky = int(input('검색할 값을 입력하세요:'))

    idx = bin_search(x, ky)

    if idx == -1:
        print('failed')
    else:
        print(f'x[{idx}]에 있다')
