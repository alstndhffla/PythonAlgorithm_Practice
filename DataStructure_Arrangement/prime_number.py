# 1,000 이하의 소수를 나열하기

# 나눗셈 횟수를 카운트
counter = 0

# 맨 처음 n = 2일 경우, 두번째 for문을 돌지 않고 바로 print(n)이 된다.
for n in range(2, 1001):
    # n이 3이 되면, i는 2까지만 하고 다음 n으로 넘어간다. range 범위가 3이라 2까지만 됨.
    for i in range(2, n):
        counter += 1
        # counter = counter + 1
        # 나누어 떨어지면 소수가 아님
        if n % i == 0:
            # 반복은 더 이상 불필요하여 중단(다음 n으로 넘어감)
            break

    # 끝까지 나누어 떨어지지 않으면 다음을 수행
    else:
        print(n)


print(f'나눗셈을 실행한 횟수: {counter}')
