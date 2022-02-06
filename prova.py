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

data = [2,6,4,7,2,3,9,6]
for i in range(len(data)):
    
    print(i)


#voglio stampare dalla 14^ riga alla 22^

#perciò

#per ogni riga nel file
#devo dare degli indici alle righe
#se l'indice della riga e compreso nel range(14,22)
#allora appendimi la riga nella lista


#come stampare un certo intervallo di righe di un file
my_file = open("shampoo_sales.txt", "r")
print(my_file.readlines()[12:14])

#_______________________________________________________________



def somma(self,a,b):
    return a+b
