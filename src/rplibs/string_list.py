def get_lengths(labels):
    l = []
    for i in labels:
        l.append(len(i))
    return l

def get_max_length(labels):
    n = get_lengths(labels)
    nmax = max(n)
    return nmax
