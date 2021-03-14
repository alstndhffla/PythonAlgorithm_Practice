# 원소의 최댓값 출력하기

# 함수에 시퀀스와 애니를 사용하기 위해 임포트함.
from typing import Any, Sequence


# 여기서 시퀀스는 시퀀스 자료형을 의미한다. 값을 받을 때 리스트, 바이트배열, 문자열, 튜플, 바이트열이 될 수 있기 때문에
# 호출하는 쪽이 넘겨주는 실제 인수의 자료형이 그 안에 있다면 무엇이든 상관없다.
# Any 는 제약이 없는 임의의 자료형을 의미. -> int 나 float 이 나와도 상관없이 반환해주겠다는 것.
# 건너받는 매개변수 a의 자료형은 Sequence 자료형들 중 하나이고, 반환하는 것은 임의의 자료형(Any) 인 함수
def max_of(a: Sequence) -> Any:
    """시퀀스형 a 요소의 최댓값을 반환"""
    maximum = a[0]
    for i in range(1, len(a)):
         if a[i] > maximum: 
            maximum = a[i]
    return maximum


if __name__ == '__main__':
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요 : '))
    x = [None] * num    # 원소 수가 num인 리스트를 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]를 입력하세요.: '))

    print(f'최댓값은 {max_of(x)}입니다.')