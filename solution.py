def solution(l):
    # Your code here
    l1=[]
    for i in l:
        a=i.split('.')
        for m,n in enumerate(a):
            a[m]=int(n)
        l1.append(a)
    l1.sort()


    l2=[]

    for j in l1:
        if len(j) is 3:
            a = str(j[0])+'.'+str(j[1])+'.'+str(j[2])
        elif len(j) is 2:
            a = str(j[0])+'.'+str(j[1])
        else:
            a = str(j[0])
        l2.append(a)

    l1=','.join(l2)
    return l1
