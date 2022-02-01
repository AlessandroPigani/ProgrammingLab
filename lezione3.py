#come aprire stampare e chiudere il contenuto di un my_file
my_file = open("shampoo_sales.txt","r")  #apro in modalità lettura
print(my_file.read())      #leggimi il file e stampamelo
my_file.close          #chiudiamo il file


filo = open("shampoo_sales.txt","r")
print(filo.read()[0:50])    #mi stampa il file fino al 50° carattere

#____________________________________________________________________
#impariamo a usare la funzione split

stringa = "ehi, ciao, come va?"
elementi = stringa.split(",") #divido la stringa in corrispondenza della ,
#dalla stringa ottengo così una lista di 3 elementi

print(elementi[1])   #oggetto di indice 1 nella lista elementi

#________________________________________________________________________

#impariamo a usare la funzione float
my_var = "5.5"
numero = float(my_var)   #mi trasforma la stringa in numero
print("numericamente: {}". format(numero))

#naturalmente non posso trasformare stringhe come giulia in numero


#____________________________________________________________________

#impariamo a usare append
mia_lista = [1,2,3]
mia_lista.append("lucio")
print(mia_lista)   #posso mettere in una stessa numeri e stringhe


#____________________________________________________________________


#stampiamo solo le vendite del file dello shampoo

vendite=[]   #mi preparo una lista vuota

mio_file = open("shampoo_sales.txt","r")
for line in mio_file:
    
    elements = line.split(",")
    
    if(elements[0]!="Date"):  #salto la prima riga del titolo
        giorno = elements[0]   
        valore = elements[1] #quando esco da questo blocco le variabili giorno e #valore non esistono più
        vendite.append(float(valore))   #passo da stringa a numero

print(vendite)    #ora ho farcito la lista vendite con i valori

tot=0

for item in vendite:
    tot = tot + item

print("somma della vendite: {}". format(tot))

mio_file.close()