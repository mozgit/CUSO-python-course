def fibo(n=2):
    u = [1]
    u.append(1)
    if n < 3:
        return 1
    for i in range(2, n + 1):
        u.append(u[i - 1] + u[i - 2])
    return u[n - 1]
