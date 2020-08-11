n,m = map(int,input().split())
if(n>3):
    print(-1)
elif(n==1):
    print(0)
else:
    l=[]
    for i in range(n):
        temp = list(map(int,list(input())))
        l.append(temp)
    # print(l)
    if(n==2):
        A = l[::]
        BU = [(A[0][i] + A[1][i]) % 2 for i in range(m)]
        odd=0
        even=0
        for i in range(m):
            if(BU[i]%2 == i%2):
                odd+=1
            else:
                even+=1
        print(min(even,odd))
    else:
        newLU = []
        newLD = []
        ans=0
        A = l[::]
        BU = [(A[0][i] + A[1][i]) % 2 for i in range(m)]
        BD = [(A[1][i] + A[2][i]) % 2 for i in range(m)]
 
        oddodd = 0
        oddeven = 0
        evenodd = 0
        eveneven = 0
        for i in range(m):
            if BU[i] == i % 2 and BD[i] == i % 2:
                oddodd += 1
            if BU[i] != i % 2 and BD[i] == i % 2:
                evenodd+=1
            if BU[i] != i % 2 and BD[i] != i % 2:
                eveneven+=1
            if BU[i] == i % 2 and BD[i] != i % 2:
                oddeven+=1
        # print(oddodd, oddeven, evenodd, eveneven)
        print(m-max([oddodd, oddeven, evenodd, eveneven]))
