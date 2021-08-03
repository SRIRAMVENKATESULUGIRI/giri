mydata=[10,15,26,32,48,64]
def result(n):
    if n<30:
        return True
    else:
        return False
    
z=[x for x in filter(result,mydata)]
print(z)