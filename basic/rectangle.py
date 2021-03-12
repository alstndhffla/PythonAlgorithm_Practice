# 넓이가 area 인 직사각형의 변의 길이(1이상인 정수) 나열하기

area = int(input('변의 길이를 구할 직사각형의 넓이를 입력하세요:'))

for i in range(1, area +1):
    if i * i > area:    # 정사각형의 넓이 이상일 때 break
        break
    if area % i:
        continue

    print(f'{i} * {area // i}')

