prezzi = []

my_file = open('shampoo_sales.txt', 'r') 
#apro il file in modalità lettura (r sta per reading)
for line in my_file:   #per ogni linea nel mio file:
    elemento = line.split(",")  
  #divido gli elementi in corrispondenza della virgola
  #un elemento comicia quando comincia la linea e finisce quando arrivo alla virgola

    if elemento[0] != "Date":  #se l'elemento di indice 0 è diverso da "date":
        Date = elemento[0]  #l'elemento prima della virgola è associato a date
        valore = elemento[1]  #l'elemento dopo la virgola è associato a values

        prezzi.append(float(valore))  
        #la funzione append mi aggiunge la variabile valore alla lista prezzi. Considerando i valori che trova nel file

#prima la lista values era vuota, ora l'ho riempita con i valori (che sono gli elementi di indice 1)

print("i valori sono i seguenti: {}".format(prezzi))

def somma(mia_lista):  
    #sto definendo una funzione somma che ha come parametro una mia lista (a cui associerò values[])
    totale = 0
    for item in mia_lista:
        totale = totale + item
    return totale
#esco dalla funzione

print("risultato: {}".format(somma(prezzi)))  
#richiamo la funzione che ha come parametro la lista values[]