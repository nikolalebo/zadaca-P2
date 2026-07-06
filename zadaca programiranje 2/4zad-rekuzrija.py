def sa_zada(string):
    if len(string)==0:
        return string
    else:
        return sa_zada(string[1:])+string[0]