
def multiplication_table(n):
    arr = []

    for i in range(1, n + 1):
        y = []
        for j in range(1, i + 1):
            y.append(i * j)
        arr.append(y)
    return arr
