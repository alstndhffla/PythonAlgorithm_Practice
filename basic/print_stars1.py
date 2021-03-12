
n = int(input("출력할 별의 갯수를 입력하세요.:"))
w = int(input("몇개까지 출력 후 줄을 바꿀건가요? :"))


print("\n")


for i in range(n):      # i는 0부터 n까지 반복(n포함 x)
    print('*', end='')
    if i % w == w - 1:  # n번 판단
        print()         # 줄바꿈

if n % w:
    print()     # 줄바꿈

