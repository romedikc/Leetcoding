def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:
    products.sort()
    output = []
    l, r = 0, len(products) - 1
    for i in range(len(searchWord)):
        char = searchWord[i]

        while l <= r and (len(products[l]) <= i or products[l][i] != char):
            l += 1

        while l <= r and (len(products[r]) <= i or products[r][i] != char):
            r -= 1
        output.append([])
        remain = r - l + 1
        for j in range(min(3, remain)):
            output[-1].append(products[l + j])
    return output


products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"
print(suggestedProducts(products, searchWord))
