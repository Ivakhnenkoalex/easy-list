def ft_len_mass(mass):
    a = 0
    for i in mass:
        a += 1
    return a


def ft_even_index_list(mass):
    i = 0
    d = ft_len_mass(mass)
    s = []
    while d > i:
        if i % 2 == 0:
            s.append(mass[i])
        i = i + 1
    return s
