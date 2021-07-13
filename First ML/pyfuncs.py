def sortHLS(mdata):
    batch = [0]*len(mdata)
    n = 0
    left = list(range(len(mdata)))
    while len(left) != 0:
        a = []
        b = [] 
        for i in left:
            if mdata['Hidden layer size'].loc[i] == mdata['Hidden layer size'].loc[left[0]]:
                a.append(i)
            else:
                b.append(i)
        left = b
        batch[n] = a
        n = n + 1
    trubatch = batch[0:n]
    return trubatch
