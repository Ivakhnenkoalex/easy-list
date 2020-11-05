def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_rev_list(mass):
    a = []
    d = ft_len(mass)
    c = d
    i = 0
    d = d - 1
    while d > i:
        a.append(mass[d])
        d = d - 1
    a.append(mass[0])
    i = 0
    while c > i:
        mass[i] = a[i]
        i = i + 1
    return mass
