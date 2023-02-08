def mcd(a,b):

    if a == b:
        return a
    else:
        return mcd(min(a,b),max(a,b)-min(a,b))


print(mcd(15,20))
