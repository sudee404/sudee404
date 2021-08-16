def filter_ints(v):
    v=filter(lambda x:x!=0,(v))
    return [num for num in v if is_positive(num)]

def is_positive(n):
    return n > 0