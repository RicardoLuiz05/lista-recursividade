def seqtermos1(n):
    if (n == 1):
        return 1

    return seqtermos1(n-1) + 1/n

print(seqtermos1(4))