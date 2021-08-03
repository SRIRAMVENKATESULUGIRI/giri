inch=[1,2,3,4]
def convert(n):
    return n*1000

z=[x for x in map(convert,inch)]
print(z)