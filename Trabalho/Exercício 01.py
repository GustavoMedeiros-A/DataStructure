def naturalSoma(n):
    if n == 1:
        return 1
    else:
        return n + naturalSoma(n - 1)

n = int(input('Qual valor deve ser somado? '))
print(naturalSoma(n))

