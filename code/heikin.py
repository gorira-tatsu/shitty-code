heikinlist = []
while True:
    k = input()
    if not k:
        print(sum(heikinlist)/len(heikinlist))
        break
    else:
        heikinlist.append(int(k))
