def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_rev_list(mass):
    d = ft_len(mass)
    return [l.pop()] + f(l) if d > 1 else l
