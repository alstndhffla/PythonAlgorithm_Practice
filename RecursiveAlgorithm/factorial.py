def factorial(n: int) -> int:
    """
    양의 정수 n 의 팩토리얼값을 재귀적으로 구함
    n! = n * (n-1)!
    :param n:
    :return:
    """
    if n > 0:
        return n * factorial(n-1)
    else:
        # 0! 은 1
        return 1


if __name__ == '__main__':
    n = int(input('출력할 팩토리얼값을 입력하세요:'))
    print(f'{n}의 팩토리얼은 {factorial(n)}입니다.')

"""
파이썬에서는 팩토리얼 값을 구하는 표준 라이브러리 math 모듈에서
factorial() 함수를 제공한다.
math.factorial(x) 는 정수 x의 팩토리얼 값을 반환한다.
"""