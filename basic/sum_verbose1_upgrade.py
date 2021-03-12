"""
기존 코드에서 else 부분은 맨 마지막 숫자를 더하기 위해서만 존재하는 코드였다.
반복문을 실행하는 동안 딱 한번만 코드가 사용되므로 굉장히 비효율적인 것임.
여기서는 그 부분만 따로 떼내서 실행시키는 것으로 업그레이드시킴.
"""

print('a부터 b 까지의 합을 구합니다.')
a = int(input('정수 a를 입력하세요.: '))
b = int(input('정수 b를 입력하세요.: '))

if a > b:
    a, b = b, a

sum = 0

for i in range(a, b):
    # end에 빈 문자열을 지정하면 다음 번 출력이 바로 뒤에 오게 됨
    print(f"{i} + ", end='')
    # print(f"{i} + ")
    sum += i

# print(f"{b} = ", end='')
print(f"{b} = ")
sum += b

print(sum)
