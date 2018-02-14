def numsort(numlist):
    newnumlist=[]
    while numlist:
        smallest_num = numlist[0] #smallest_num should be at the 0 position of the list
        for x in numlist:
            if x < smallest_num:
                smallest_num = x
        newnumlist.append(smallest_num)
        numlist.remove(smallest_num)
    print(newnumlist)


numlist=[67, 45, 2, 13, 1, 998]
numsort(numlist)


numlist=[89, 23, 33, 45, 10, 12, 45, 45, 45]
numsort(numlist)



