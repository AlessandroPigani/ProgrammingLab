lista = [1,2,3,6,8,3]
print(lista)

print(lista[1:2])
print(lista[0:-1])

print(lista[1:None])
print(lista[1:])


inizio = ["2","4","8", "23"]
fine = []

for i,element in enumerate(inizio):
    if(i==0): fine.append(inizio[0])
    
    else:
        inizio[i] = float(inizio[i])
        fine.append(inizio[i])

print(fine)





    