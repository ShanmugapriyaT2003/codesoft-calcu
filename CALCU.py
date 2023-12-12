A=int(input("enter the number:"))
B=int(input("enter the number:"))
choose=input("enter the chose:")
if choose == 'add':
    print(A+B)
elif choose =='sub':
    print(A-B)
elif choose =='mul':
    print(A*B)
elif choose =='div':
    print(A/B)
else:
    print(A%B)


