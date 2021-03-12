print("+, - 을 번갈아 출력합니다.")

n = int(input("몇 개를 출력할까?:"))

for i in range(n):
    if i % 2:
        print("-", end="")
    else:
        print("+", end="")

print()