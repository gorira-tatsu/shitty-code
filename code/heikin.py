heikinlist = []
s = 0
while True:
    k = input()
    if not k:
        l = len(heikinlist)
        for i in range(l):
            s = s + heikinlist[i]
        print(s/l)
        break
    else:
        heikinlist.append(int(k))
