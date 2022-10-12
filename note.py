n1= int (input("Entrer votre note 1 "))
n2= int (input("Entrer votre note 2 "))
n3= int (input("Entrer votre note 3 "))
n=(n1 + n2 + n3)/3
if n > 16:
    print("Très bien")
elif n < 16 and n >= 14:
    print("Bien")
elif n < 14 and n >= 12:
    print("Assez bien")
elif n < 12 and n >= 10:
    print("Passable")
else:
    print("Insuffisant")