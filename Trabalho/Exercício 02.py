def somaAlgarismos(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + somaAlgarismos(n // 10)


n = int(input("Digite o número que você quer somar: "))
print(somaAlgarismos(n))