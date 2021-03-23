# 순수 재귀 함수 구현

def recur(n: int) -> int:
    """
    :param n:
    :return:
    """
    if n > 0:
        # 함수안에서 재귀 호출을 2번 실행한다.
        # 재귀 호출을 여러번 실행하는 함수를 순수한 재귀라고 한다.
        recur(n-1)
        print(n)
        recur(n-2)


x = int(input('정숫값을 입력하세요:'))

recur(x)


