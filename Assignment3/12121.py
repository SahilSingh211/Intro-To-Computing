a=input("Enter :")
a=a.lower()
L=[]
if " " not in a:
    for char in a: 
        c=(char,a.count(char))
        L.append(c)
    sett=set(L)
    L1=list(sett)
    L1.sort()
    print(L1)


        #second part- list full string and then .count
else:
    b=a.split()
    for character in b:
        print(character,"=",b.count(character))


    



    
