def addBinary(self, a: str, b: str) -> str:
    def binaryToDecimal(n):
        return int(n, 2)

    def decimalToBinary(n):
        return bin(n).replace("0b", "")

    output = binaryToDecimal(a) + binaryToDecimal(b)
    return decimalToBinary(output)


a = "11"
b = "1"
print(addBinary(a, b))
