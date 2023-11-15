age=int(input(" enter Amal's age:"))
S=0
for i in range(1,age+1):
    S=S+(500+(i*3))
print("Amal's account at",age,"years is",S)