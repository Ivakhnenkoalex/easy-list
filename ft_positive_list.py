def ft_len_mass(mass):
    a = 0
    for i in mass:
        a += 1
    return a


def ft_positive_list(mass):
    i = 0
    d = ft_len_mass(mass)
    k = 0
    while d > i:
        if mass[i] > 0:
            k = k + 1
        i = i + 1
    return k
