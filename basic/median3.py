def median3(a, b, c):
    if a >= b:
        if b > c:
            return b
        elif a <= c:
            return a
        else:
            return c

    elif a > c:
        return a

    elif b > c:
        return c

    else:
        return b


a = int(input("중앙값을 비교할 수를 입력하세요."))
b = int(input("중앙값을 비교할 수를 입력하세요."))
c = int(input("중앙값을 비교할 수를 입력하세요."))

print(f"중앙값은 {median3(a, b, c)}")