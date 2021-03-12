
# 변수가 하나일 때는 while 문 보다 for 문을 사용하는게 더 좋다

n = int(input("더할 정수를 입력하세요: "))

sum = 0

for i in range(1, n+1):
    sum += i

print(f"총 합은 {sum}")