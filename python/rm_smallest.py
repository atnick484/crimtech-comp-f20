def rm_smallest(d):
    if len(d) == 1 or len(d) == 0:
        return d
    keys = list(d.keys())
    minKey = keys[0]
    for x in d:
        if d[x] < d[minKey]:
            minKey = x
    d.pop(minKey)
    return d

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()