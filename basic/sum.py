print("a부터 b까지 정수의 합을 구해요")

a = int(input("정수 a를 입력하세요:"))
b = int(input("정수 b를 입력하세요:"))

if a > b:

    # 단일대입문
    # a 가 b보다 크기 때문에 각각 교환한다. a 는 b 로, b 는 a 로 동시 바인딩
    a, b = b, a

sum = 0

# 범위 a 이상 b 미만
for i in range(a, b+1):
    sum += i

print(f"{a}부터 {b}까지의 합은 {sum}입니다.")