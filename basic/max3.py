print("세 정수 중 최대값(가장 큰 값) 구하기")
a = int(input('정수1 을 입력하세요:'))
b = int(input('정수2 을 입력하세요:'))
c = int(input('정수3 을 입력하세요:'))

maximum = a
if b > maximum:
    maximum = b
if c > maximum:
    maximum = c

print("최대값은 ", maximum)
print(f"최대값은 {maximum}")