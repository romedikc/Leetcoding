def evenOddBit(n: int) -> List[int]:
    b = bin(n)[2:]
    even, odd = 0, 0
    for i in range(len(b) - 1, -1, -1):
        if b[i] == '1' and (len(b) - i) % 2 == 0:
            even += 1
        elif b[i] == '1' and (len(b) - i) % 2 != 0:
            odd += 1
    return [even, odd][::-1]


n = 17
print(evenOddBit(n))
