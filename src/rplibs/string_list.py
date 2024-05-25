def get_lengths(labels):
    l = []
    for i in labels:
        l.append(len(i))
    return l

def get_max_length(labels):
    n = get_lengths(labels)
    nmax = max(n)
    return nmax

def print_table(type, stores, sales):
    spaces = ' ' * get_max_length(stores) + ' '
    print(spaces, 'Sales')
    print('Stores', end='\t')
    for i in type:
        print(i, end='\t')
    print()
    for i in sales:
        print(i, end='\t')
        for j in sales[i]:
            print(j, end='\t')
        print()
