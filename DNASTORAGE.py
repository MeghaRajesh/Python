T=int(input())
for i in range(T):
    N=int(input())
    output=""
    s=input()
    if(N%2==0):
        for r in range(0,len(s),2):
            newStr=s[r:r+2]
          
            if(newStr=="00"):
                output+="A"
            elif(newStr=="01"):
                output+="T"
            elif(newStr=="10"):
                output+="C"
            else:
                output+="G"
        print(output)