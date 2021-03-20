from typing import Any, Sequence


def seq_search(a: Sequence, key: Any) -> int:
    """
    for 문을 활용한 선형 검색
    선형검색은 원소의 값이 정렬되지 않은 배열에서 검색할 때 사용하는 유일한 방법.
    """

    for i in range(len(a)):
        if a[i] == key:
            return i    # 검색 성공

    return -1   # failed


if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요:'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]:'))

    ky = int(input('enter the search value:'))

    # 리턴값으로 i or -1 이 들어온다.
    idx = seq_search(x, ky)

    if idx == -1:
        print('there is no value you are looking for')
    else:
        print(f'search value is x[{idx}]')