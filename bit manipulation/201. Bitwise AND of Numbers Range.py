def rangeBitwiseAnd(left: int, right: int) -> int:
    shift = 0
    while left < right:
        # Repeat until left and right
        # are equal or differ by only one bit.
        left >>= 1  # Right-shift by 1 bit
        right >>= 1  # Right-shift by 1 bit
        shift += 1
    return left << shift


left = 5
right = 7
print(rangeBitwiseAnd(left, right))
