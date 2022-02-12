
Gradelist={ 'A+':"Outstanding", 'A':"Excellent", 'B+':'Very Good', 'B':'Good', 'C+':'Average', 'C':'Below Average', 'D':'Poor'}

def marks(a,b):
    return("Your Grade is '{0}' and {1} performance.".format(a,b))
grade=int(input("Enter your grade :"))
if grade<=3:
    print("invalid grades")
elif grade==4:
    a='D'
elif grade==5:
    a='C'
elif grade ==6:
    a='C+'
elif grade==7:
    a='B'
elif grade==8:
    a='B+'
elif grade==9:
    a='A'
elif grade==10:
    a='A+'
b=Gradelist[a]

print(marks(a,b))




