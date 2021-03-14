# 원소의 최댓값 출력하기(원소값은 난수로 생성)

import random   # 난수 생성을 위한 임포트
from max import max_of  # 같은 폴더 내에 위치한 모듈로부터 함수 임포트

print('난수의 최댓값을 구합니다.')
num = int(input('난수의 개수를 설정하세요.: '))
low = int(input('난수의 최솟값을 설정하세요.: '))
high = int(input('난수의 최댓값을 설정하세요.: '))

# 원소 수 num인 리스트를 생성
x = [None] * num

for i in range(num):
    x[i] = random.randint(low, high)

print(f'{(x)}')
print(f'최댓값은 {max_of(x)}입니다.')