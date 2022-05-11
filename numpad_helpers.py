# _pair
def _pair(dec):
    power = 0
    while dec % 1 and power < 10:
        power -= 1
        dec *= 10
    return [int(dec), power]
# _pair


# eq
def eq(e1, e2):
    if type(e1) == type(e2):
        return e1 == e2
    elif isinstance(e1, list) and isinstance(e2, int):
        return len(e1) == e2
    elif isinstance(e1, int) and isinstance(e2, list):
        return e1 == len(e2)
    assert False
# eq


# gt
def gt(e1, e2):
    if type(e1) == type(e2):
        return e1 > e2
    elif isinstance(e1, list) and isinstance(e2, int):
        return len(e1) > e2
    elif isinstance(e1, int) and isinstance(e2, list):
        return e1 > len(e2)
    assert False
# gt


# lt
def lt(e1, e2):
    if type(e1) == type(e2):
        return e1 < e2
    elif isinstance(e1, list) and isinstance(e2, int):
        return len(e1) < e2
    elif isinstance(e1, int) and isinstance(e2, list):
        return e1 < len(e2)
    assert False
# lt


# add
def add(e1, e2):
    if isinstance(e1, int) and isinstance(e2, int):
        return e1 + e2
    elif isinstance(e1, list):
        return e1 + [e2]
    assert False
# add


# sub
def sub(e1, e2):
    if isinstance(e1, int) and isinstance(e2, int):
        return e1 - e2
    elif isinstance(e1, list) and isinstance(e2, int):
        return e1[:e2] + e1[e2+1:]
    assert False
# sub


# mul
def mul(e1, e2):
    if isinstance(e1, int) and isinstance(e2, int):
        return e1 * e2
    elif isinstance(e1, list) and isinstance(e2, list):
        return e1 + e2
    assert False
# mul


# div
def div(e1, e2):
    if isinstance(e1, int) and isinstance(e2, int):
        return _pair(e1 / e2)
    elif isinstance(e1, list) and isinstance(e2, int):
        return e1[e2]
    assert False
# div


# rem
def rem(e1, e2):
    if isinstance(e1, int) and isinstance(e2, int):
        return e1 % e2
    elif isinstance(e1, list) and isinstance(e2, int):
        return e1[e2:]
    elif isinstance(e1, list) and isinstance(e2, list):
        return all(i in e1 for i in e2)
# rem


# flr
def flr(e1, e2):
    if isinstance(e1, int) and isinstance(e2, int):
        return e1 // e2
    elif isinstance(e1, list) and isinstance(e2, int):
        return e1[:e2]
    elif isinstance(e1, list) and isinstance(e2, list):
        return all(i in e2 for i in e1)
# flr
