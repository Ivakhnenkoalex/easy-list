def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_rev_par_list(mass):
    d = ft_len(mass)
    i = 1
    r = []
    if d % 2 == 0:
        while d > i:
            r.append(mass[i])
            r.append(mass[i-1])
            i = i + 2
        return r
    else:
        d = d - 1
        while d > i:
            r.append(mass[i])
            r.append(mass[i-1])
            i = i + 2
        r.append(mass[d])
        return r