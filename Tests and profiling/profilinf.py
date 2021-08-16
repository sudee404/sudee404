#finding pythagorean triples
def is_int(n):
    return n==int(n)

def calc_hp(a,b):
    return(a*a + b*a)**.5

def calc_tripples(m):
    triples=[]
    for a in range (1,m+1):
        for b in range(a,m+1 ):
            c=calc_hp(a,b)
            if is_int(c):
                triples.append((a,b,int(c)))
    return (triples)

tripples=calc_tripples(1000)
