n = int(input("1부터 n까지 정수의 합을 구합니다. n 값을 입력하세요: "))

sum = 0
i = 1

# i 가 n 보다 작거나 같을때까지 계속 반복
while i <= n:
    sum += i
    i += 1

print(f"합계는 {sum}입니다.")