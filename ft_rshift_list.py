def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return (a)


def ft_rshift_list(mass):
    d = ft_len(mass)
    r = []
    r.append(mass[d - 1])
    i = 1
    d = d - 1
    r.append(mass[0])
    while d > i:
        r.append(mass[i])
        i = i + 1
    return r
