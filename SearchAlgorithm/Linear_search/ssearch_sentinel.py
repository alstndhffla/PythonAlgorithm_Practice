from typing import Any, Sequence
import copy


def seq_search(seq: Sequence, key: Any) -> int:
    """
    시퀀스에서 key와 일치하는 원소를 선형 검색(보초법)
    매번 값이 있는지 혹은 배열을 다 뒤지고 나서 종료해야했는데
    배열 맨 끝에 내가 찾고자 하는 값을 넣어줌으로써 값이 있는지만 판단하므로
    종료조건이 줄어든다(과정 간소화)
    while 문의 if 문을 두 번써서 판단하는 것 대비 2배나 줄어든다. return 을 반환할때만 과정이 딱 1번 추가되고.
    """
    a = copy.deepcopy(seq)  # 아예 새로운 객체로 깊은 복사
    a.append(key)   # 보초 키값 추가

    i = 0
    # 배열 원소를 스캔해 검색하는 과정 반복
    while True:
        if a[i] == key:
            break   # 검색성공시 while 문 종료
        i += 1

    # 검색실패시 -1 반환(시퀀스의 길이와 찾으려는 i 값이 같다는 소리는 보초값을 찾았다는 것이므로)
    # 그렇지 않게 종료시 i 값 반환(break 시 해당 i 값)
    return -1 if i == len(seq) else i


if __name__ == '__main__':
    num = int(input('원소수를 입력하세요:'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]'))

    ky = int(input('검색할 값을 입력하세요:'))

    idx = seq_search(x, ky)

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있다.')