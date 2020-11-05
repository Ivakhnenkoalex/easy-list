def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_super_shift_list(mass, n):
    d = ft_len(mass)
    r = []
    c = d
    i = 0
    if n >= 0:
        while n > i:
            r.append(mass[d - 1])
            d = d - 1
            i = i + 1
        i = 0
        while c - n > i:
            r.append(mass[i])
            i = i + 1
        return r
    else:
        i = n - n * 2
        while i < d:
            r.append(mass[i])
            i = i + 1
        i = 0
        while i > n:
            r.append(mass[i - i * 2])
            i = i - 1
        return r
