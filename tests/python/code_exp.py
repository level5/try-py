import pprint


# 把一个list分割成小的lists
l = range(10, 75)
n = 10


# 使用generator比较好:
def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]


pprint.pprint(list(chunks(l, n)))

pprint.pprint([l[i:i+n] for i in range(0, len(l), n)])


# 把list in list合并成一个list
l = [[12], [13, 14], [], [15, 16, 17, 18], [19]]
pprint.pprint([val for values in l for val in values])

l = [11, [12], [13, 14], [], 15, [16, 17, 18], [19], 20, 21]


def flatten(l):
    if type(l) is int:
        yield l
    else:
        for val in l:
            yield from flatten(val)

pprint.pprint(list(flatten(l)))


