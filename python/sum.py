def sum(lst, n):
    i = 0
    for x in lst:
        j=0
        for y in lst:
            if i == j:
                continue
            elif (x + y == n):
                return True
            j += 1
        i += 1
    return False

def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()