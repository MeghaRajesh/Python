n=1
while(n>0):
    n=int(input())
    if(n>0):
        ambiguous=True
        p=list(map(int,input().split()))   
        for i in range(n):
            if(p[p[i]-1]!=i+1):
                ambiguous=False
                break
        if(ambiguous):
            print("ambiguous")
        else:
            print("not ambiguous")