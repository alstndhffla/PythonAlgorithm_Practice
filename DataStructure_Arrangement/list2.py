x = ['john', 'george', 'paul', 'ringo']

# enumerate - 자료형의 현재 순서(index)와 그 값을 알 수 있다.
# ()안에 먼저, 참조할 자료형을 입력하고 맨 첫 요소에 몇번을 부여할건지 입력한다.
for i, name in enumerate(x, 1):
    print(f'{i}번째 = {name}')