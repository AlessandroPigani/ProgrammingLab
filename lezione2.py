print("Hello world")


parola = "sarusso"
print(parola)

lista = ["Luca", "Mario"]
print(lista[1])  #estrapolo l'elemento 1

for item in lista:    #potrei fare direttamente print(lista)
    print(item) 


print("nome 1:{}, nome 2:{}". format(lista[0], lista[1]))

lista = lista + ["gianni"]
print(lista)

lista = lista + [13,17]
print(lista)

#stampo la lista dal primo al penultimo termine
print(lista[0:-1])

if "gianni" in lista:
    print("proprio luiiiiii")

else: print("non vaaa")

if "Mattia" in lista:
    print("proprio luiiiiii")

else: print("non vaaa")

#_________________________________________________________________________


for samarcanda in range(10):   
    print(samarcanda)  #posso chiamare gli elementi come cavolo voglio


dizionario = {"luogo": "Palmanova", "data": 110602}
print(dizionario["data"])

#data è la chiave. 110602 è il valore

#_________________________________________________________________________

def funz(arg1, arg2):
    print("argomenti: {} {}". format(arg1, arg2))

#chiamo la funzione (ISTANZIAZIONE)
funz("pippo", "pluto")  #saranno arg1 e arg2


#________________________________________________________________________

#ESERCIZIO PER CASA
#SCRIVERE UNA FUNZIONE CHE SOMMI I NUMERI DI UNA lista

def somma(my_list):
    tot=0
    for item in my_list:
        tot = tot + item
    return tot

numeri = [45,64,746,23]

print("risultato: {}". format(somma(numeri)))
#così mi stampo anche in maniera elegante il risultato