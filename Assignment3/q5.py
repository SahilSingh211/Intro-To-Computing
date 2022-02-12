n1=0
n2=1
count=0
L=[]
nterm=int(input("Enter Your Number of terms :"))
if nterm<=0:
    print("enter valid number")
elif nterm>=1:
    if nterm==1:
        print("Your Number Is :",n1)
    else:
        while nterm>count:
            nth=n1+n2
            L.append(n1)
            d=sum(L)
            print(n1)
            n1=n2
            n2=nth
            count+=1
    print(d/nterm)

