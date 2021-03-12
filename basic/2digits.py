# 두자리 양수만 입력받기

while True:
    n = int(input('숫자를 입력하세요:'))

    # 종료조건(반복문을 종료하기 위한 조건)
    # if n >= 10 and n <= 99:
    if 10 <= n <= 99:
        break

print(f'입력받은 수는 {n}')