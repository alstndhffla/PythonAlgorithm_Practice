# 1부터 12까지 8만 스킵하고 출력.
# 리스트를 사용하여 범위를 미리 정해 8만 건너뛰고 반복하게 만듦.
# for 문 반복을 위한 연산비용은 여전히 발생한다.
for i in list(range(1, 8)) + list(range(9, 13)):
    print(i, end='')

print()