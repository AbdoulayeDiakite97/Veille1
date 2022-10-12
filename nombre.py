a = int (input("Entrer un nombre entier n "))
b= [i for i in range(10)]
for i in b:
    print("{} * {} = {}".format(a,i,a*i))