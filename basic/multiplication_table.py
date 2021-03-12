# 다중루프 - 구구단

# 1 ~ 9 까지.
for i in range(1, 10):      # (세로방향) 루프(1, 2, 3, 4행...)
    for j in range(1, 10):  # (가로방향) 루프
        # i * j 를 3자리로 출력 - 3자리를 주어야 가지런히 출력됨
        print(f'{i * j : 3}', end='')
        # print(f'{i * j}', end='')
    # 행 변경
    print()
