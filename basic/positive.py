print("양수만을 입력받아 1부터 n까지의 합을 구하세요")

while True:
    n = int(input("n값을 입력하세요:"))
    # n 값이 0보다 커야하므로(양수) 음수일 경우 지속적으로 값을 입력받도록 함.
    if n > 0:
        break   # 양수 입력시 반복문 종료.

sum = 0
i = 1

for i in range(1, n+1):
    sum += i
    i += 1

print(f'1부터 {n}까지의 합은 {sum} 입니다.')