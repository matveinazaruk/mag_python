from itertools import groupby

def pairs(l):
    for i in range(0, len(l), 2):
        yield l[i:i + 2]

def compress(data):
    for k, g in groupby(data):
        yield len(list(g))
        yield k

def uncompress(data):
    if len(data) % 2 != 0:
        raise ValueError("List should be even length.")
    for k, v in pairs(data):
        if isinstance(k, int):
            for _ in range(k):
                yield v
        else:
            raise ValueError("List has wrong structure.")


testlist = ["a", "b", "b", "c", "b", "c", "c"]
print( testlist)
testlistgrpd = list(compress(testlist))
print(testlistgrpd)
print(list(uncompress(testlistgrpd)))
