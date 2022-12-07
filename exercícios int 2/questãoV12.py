def seqTermos2(n):
    if (n == 1):
        return 1

    else:
        return ((((n-1) * n-1) + 1) / (n-1) + 3) + (((n*n) + 1) / (n+3)) + seqTermos2(n-1)

print(seqTermos2(4))