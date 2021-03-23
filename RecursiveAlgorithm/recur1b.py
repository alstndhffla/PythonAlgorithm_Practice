# 스택으로 재귀 함수 구현하기(재귀를 제거)
# 비재귀적으로 표현하는 방법 중 하나로 재귀호출되는 함수를 제거(재귀를 제거)
# 스택을 활용해 재귀를 제거한 코드를 사용한다.

from stack import Stack  # stack.py의 Stack 클래스를 임포트


def recur(n: int) -> int:
    """재귀를 제거한 함수 recur"""
    s = Stack(n)

    while True:
        if n > 0:
            s.push(n)         # 입력된 n 값을 푸시
            n = n - 1
            continue          # 다시 while 문 처음으로 돌아감
        if not s.is_empty():  # 첫번째 if 문을 만족하지 못한 상태, 스택이 비어 있지 않으면
            n = s.pop()       # 저장하고 있는 값을 n에 팝
            print(n)
            n = n - 2
            continue          # 다시 while 문 처음으로 돌아감
        break


x = int(input('정수값을 입력하세요.: '))

recur(x)
