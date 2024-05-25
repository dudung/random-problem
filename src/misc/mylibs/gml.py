def get_max_length(labels):
    n = 0
    for l in labels:
        if len(l) > n:
            n = len(l)
    return n
