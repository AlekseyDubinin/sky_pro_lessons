def hashword(word: str, size=1000) -> int:
    hash_value = 0
    for s in word:
        hash_value += ord(s)
    return hash_value % size


def hashfloat(num: float, size=1000) -> int:
    fraction = abs(num - int(num))
    fraction = int(str(fraction)[2:])
    hash_value = (int(num) + fraction) % size
    return hash_value

print(hashword('apple'))
print(hashword('orange'))
print(hashword('apricot'))
print(hashfloat(125.367859))
print(hashfloat(125.367858))
print(hashfloat(-378.127856321))
