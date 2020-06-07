heikinlist = []
d = 0
e = 0
while True:
    a = input()
    if not a:
        b = len(heikinlist)
        for j in range(b):
            c = heikinlist[d]
            e = c + e
            d = d + 1
        e = e / d
        print(e)
        break
    else:
        heikinlist.append(int(a))