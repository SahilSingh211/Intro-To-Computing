Gradelist={ '10':['A+',"Outstanding"], '9':['A',"Excellent"], '8':['B+','Very Good'], '7':['B','Good'], '6':['C+','Average'],'5': ['C','Below Average'], '4':['D','Poor']}
def marks(a):
    for a,b in Gradelist:
        Gradelist[a]=b
        print(b)

        return("Your Grade is", b[0],"and",b[1], "performance.")
        
        
Grade=(input())
print(marks(Grade))


     

        
        

