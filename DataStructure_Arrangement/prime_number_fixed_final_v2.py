# 직전 파일에서는 리스트의 크기를 지정했는데 여기서는 따로 지정하지 않고
# 소수가 생기는대로 추가하는 방식이다..

counter = 0

prime = [2, 3]


for n in range(5, 1001, 2):
    i = 1
    # 어떤 정수 n 은 n의 제곱근 이하의 어떤 소수로도 떨어지지 않는다.
    # 제곱근을 구하기 보다 n * n 을 활용하는게 더 쉬움으로 이를 활용함.

    while prime[i] * prime[i] <= n:
        counter += 2    # 위 코드의 곱셈과 아래 코드 나눗셈을 계산하기 때문에 2를 카운트
        if n % prime[i] == 0:
            break
        i += 1

    else:   # 끝까지 나누어 떨어지지 않았으면 소수로 추가한다.
        prime += [n]
        counter += 1

for i in prime:
    print(i)

print(f'곱셈과 나눗셈을 실행한 횟수: {counter}')

