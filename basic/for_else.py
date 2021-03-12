import random

n = int(input('생성할 난수의 개수를 입력:'))

# n 이 10 일 경우, 0 ~ 9 까지 총 10번 반복
for _ in range(n):
    # 10부터 99까지 정수를 랜덤생성.
    r = random.randint(10, 99)
    print(r, end=',')

    # 랜덤으로 생성된 수가 13이 되면
    if r == 13:
        print('\n 프로그램 종료.')
        break   # else 문을 안거치고 지나간다.

# 10번을 다 채우면 아래코드를 진행325 
else:
    print('\n 난수 생성 종료.')
