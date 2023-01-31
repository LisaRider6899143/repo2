n = int(input())
seqSum = 0
i = 1
while n != 0:
    if n % 2 == 0:
        seqSum += n
        i = i+1
        n = int(input())
    else:
        n = int(input())
print(i-1)
