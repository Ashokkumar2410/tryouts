def permute(list, s):
    if list == 1:
        return s
    else:
        return [ y + x
                 for y in permute(1, s)
                 for x in permute(list - 1, s)
                 ]
def permutations(s):
    if not s:
        yield []
    yield from ([s[i], *p] for i in range(len(s)) for p in permutations(s[:i] + s[i + 1:]))