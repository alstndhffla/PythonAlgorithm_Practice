# max_of 함수 임포트 시켜 사용하기.
from max import max_of

print('배열의 최댓값을 구합니다. 비교를 원하는 숫자를 입력하시고 End 룰 입력해 확인하세요.')

number = 0
x = []                  # 빈 리스트

while True:
    s = input(f'x[{number}]를 입력하세요.: ')
    if s == 'End':
        break
    x.append(int(s))    # 배열의 끝에 추가
    number += 1

print(f'{number}개를 입력했습니다.')
print(f'최댓값은 {max_of(x)}입니다.')