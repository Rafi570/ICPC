def solve(ll):
    llist=[]
    le=len(ll)
    for i in range(0,le):
        for j in range(i,le):
            ll1=[]
            for k in range(i,j+1):
                ll1.append(ll[k])
            if len(set(ll1)) != 1 :
                llist.append(ll1)
    print(llist)
    return len(llist)





for i in range (int(input())):
    el=int(input())
    arr=map(int,input().split())
    print(solve(list(arr)))
