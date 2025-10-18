def remakeTuple(tpl, elem):
    tList = list(tpl)

    if elem in tList:
        tList.remove(elem)

    return tuple(tList)

print(remakeTuple((1, 2, 3, 2, 4), 2))