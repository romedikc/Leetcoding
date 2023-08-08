def compress(chars: List[str]) -> int:
    i = 0
    arr = []
    while i < len(chars):
        count = 1

        while i + 1 < len(chars) and chars[i] == chars[i + 1]:
            count += 1
            i += 1

        arr.append(chars[i])
        if count > 1:
            arr.extend(list(str(count)))
        i += 1

    chars.clear()
    chars.extend(arr)
    return len(chars)


chars = ["a", "a", "b", "b", "c", "c", "c"]
print(compress(chars))
