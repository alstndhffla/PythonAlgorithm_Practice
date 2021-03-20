from typing import Any, Sequence


def seq_search(a: Sequence, key: Any) -> int:
    # 시퀀스 a 에서 key 와 값이 같은 원소를 선형 검색(while)
    i = 0

    while True:
        if i == len(a):
            return -1   # 검색 실패시 -1 반환
        if a[i] == key:
            return i    # 검색에 성공하여 현재 검사한 배열의 인덱스를 반환

        i += 1


if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요:'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]:'))

    ky = int(input('enter the search value:'))

    idx = seq_search(x, ky)

    if idx == -1:
        print('there is no value you are looking for')
    else:
        print(f'search value is x[{idx}]')
