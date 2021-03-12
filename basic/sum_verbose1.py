

print('a부터 b 까지의 합을 구합니다.')
a = int(input('정수 a를 입력하세요.: '))
b = int(input('정수 b를 입력하세요.: '))

if a > b:
    a, b = b, a

sum = 0
# b - a번 반복
for i in range(a, b + 1):
    # i가 b보다 작으면 합을 구하는 과정을 출력.
    # 출력의 끝을 지정할 수 있다 -> end= '' -> 아무것도 없는게 출력의 끝임 # end에 빈 문자열을 지정하면 다음 번 출력이 바로 뒤에 오게 됨
    if i < b:
        print(f'{i} + ', end='')
    # i가 b보다 크거나 같으면 최종값 출력을 위해 i =를 출력(i 가 10 일 경우 실행되는 코드)
    else:
        print(f'{i} = ', end='')
    sum += i

print(sum)
