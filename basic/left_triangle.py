# 왼쪽 직각 이등변 삼각형 * 로 출력.

n = int(input('짧은 변의 길이를 입력:'))

# i 는 0부터 시작됨
for i in range(n):
    for j in range(i + 1):
        print('*', end='')

    # print('\n')
    print()
