# 재귀 함수의 구현(꼬리 재귀를 제거)

def recur(n: int) -> int:
    """꼬리 재귀를 제거한 함수 recur"""
    while n > 0:
        recur(n - 1)
        print(n)
        # 직전 스크립트에 있던 recur(n-2) 코드(->꼬리재귀)를 아래와 같이 바꾼 것
        # => 비재귀적으로 나타내는 방법 중 하나
        n = n - 2


x = int(input('정수값을 입력하세요.: '))

recur(x)
