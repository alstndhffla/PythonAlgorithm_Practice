# 유클리드 호제법으로 최대 공약수 구하기

def gcd(x: int, y: int) -> int:
    """
    정숫값 x와 y의 최대 공약수를 반환
    :param x:
    :param y:
    :return:
    """
    if y == 0:
        return x
    else:
        # 재귀함수로서 y 가 0 이 나올때까지 계속 반복되는거임.
        return gcd(y, x % y)


if __name__ == '__main__':
    print('두 정숫값의 최대 공약수를 구한다.')
    x = int(input('첫 번째 정숫값을 입력하세요:'))
    y = int(input('두 번째 정숫값을 입력하세요:'))

    print(f'두 정숫값의 최대 공약수는 {gcd(x, y)}')

# 계산 결과는 10이다. 애초에 나눠지지 않기 때문에 나머지 자체가 10인거임
print(10 % 20)

"""
파이썬에서는 최대 공약수를 구하는 표준 라이브러리로 math 모듈에서
gcd() 함수를 제공한다.
ex. math.gcd(a, b)
"""