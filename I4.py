def entries(tpl, id):
    if id not in tpl:
        return tuple()
    
    fInd = tpl.index(id)

    try:
        secInd = tpl.index(id, fInd + 1)
        return tpl[fInd : secInd+1]
    except ValueError:
        return tpl[fInd:]
    
officeEntries = (101, 102, 103, 101, 104, 105, 102, 106)
print(entries(officeEntries, 101))