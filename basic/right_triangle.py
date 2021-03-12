# 오른쪽 직각 이등변 삼각형 * 로 출력.

n = int(input('짧은 변의 길이를 입력:'))

# i 는 0부터 시작됨
for i in range(n):              # 행 루프
    for _ in range(n - i - 1):  # 열 루프(공백 출력)
        print(' ', end='')
    for _ in range(i + 1):
        print('*', end='')      # 열 루프(* 출력)
    print()
