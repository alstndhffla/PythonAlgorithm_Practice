# 8퀸 문제 알고리즘
# 퀸이 행과 열 방향으로 겹치지 않는 조합을 나열하는 프로그램.
# 체스에서 퀸은 대각선 방향으로 이동할 수 있으므로 어떤 대각선에서 보더라도 퀸을 1개만 배치하는 작업을 추가로 적용

pos = [0] * 8          # 각 열에 배치한 퀸의 위치
flag_a = [False] * 8   # 각 행에 퀸을 배치했는지 체크
flag_b = [False] * 15  # 대각선 방향(오위왼아)(↙↗)으로 퀸을 배치했는지 체크
flag_c = [False] * 15  # 대각선 방향(왼위오아)( ↘↖)으로 퀸을 배치했는지 체크


def put() -> None:
    """각 열에 배치한 퀸의 위치를 출력"""
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()


def set(i: int) -> None:
    """i 열의 알맞은 위치에 퀸을 배치"""
    for j in range(8):
        if(     not flag_a[j]            # j행에 퀸이 배치 되지 않았다면
            and not flag_b[i + j]        # 대각선 방향(오위왼아)으로 퀸이 배치 되지 않았다면
            and not flag_c[i - j + 7]):  # 대각선 방향(왼위오아)으로 퀸이 배치 되지 않았다면
            pos[i] = j  # 퀸을 j행에 배치
            if i == 7:  # 모든 열에 퀸을 배치하는 것을 완료
                put()
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = True
                set(i + 1)  # 다음 열에 퀸을 배치
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = False


set(0)  # 0열에 퀸을 배치