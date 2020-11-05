def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_rev_list(mass):
    a = ''
    for i in range(-1, -ft_len(str) - 1, -1):
        a += str[i]
    return a
