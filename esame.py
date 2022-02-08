class ExamException(Exception):

    pass


class CSVTimeSeriesFile():
    
    def __init__(self,arg1):

        self.name = arg1     
        #l'attributo sopravvive all'uscita dalla funzione


    def get_data(self):
        listone = [] #mi preparo una lista in cui inserirò listini di data in stinga e passeggeri in numero

        my_file = open(self.name,"r")

        for line in my_file:
            elements = line.split(",")

            if(elements[0]!="date"):
                elements[1] = float(elements[1])

                listone.append(elements)  #inserisco nel listone sia elements[0] (le date) sia elements[1] (i passeggeri)

        my_file.close()

        return listone

time_series_file = CSVTimeSeriesFile("data.csv")  #istazio l'oggetto

time_series = time_series_file.get_data()
#in questa variabile mi salvo il listone
print(time_series)

def compute_avg_monthly_difference(listone, first_year, last_year):
    #time series è il listone
    #first year è inizio intervallo
    #last year è la fine intervallo

    for i,element in enumerate(listone):   #itero sulla lista
        listone[i] = listone[i][1]  #considero solo il numero di passaeggeri. non mi servono le date

    #tanto so che ogni 12 valori si passa all'anno successivo

    #spacchettiamo, da un listone devo avere delle liste
    #una lista per anno
    for i,item in enumerate(listone): #per ogni listino in time_series
            
        lista = []
       
                   #start     #stop    #step
        for i in range(0, len(listone), 12):   #RIVEDERE PASSAGGIO
            lista.append(listone[i : i+12])  #appendi le 12 coppie di valori

    print(lista)   #all'interno del listone ho creato delle liste, ogni lista interna al listone contiene i dati di un anno

    
    #la funzione int me li trasforma in interi
    #non posso mettere float
    #altrimenti mi darebbe errore nello slicing
    first_year = int(first_year) - 1949  #anno di partenza
    last_year = int(last_year) - 1949 
    
     
    print(first_year) #inutile
    print(last_year)
    
    lista = lista [first_year : last_year+1]   #slicing
    #taglio la lista dove mi interessa, gli anni interessati

    print("_________________________________________________________")

    print(lista)  #nuova. dove c'è ciò che mi interessa
    print(lista[0])  #benissimo, posso iterare sulla lista per individuar gli anni 

    print("_________________________________________________________")

    
    lista_finale = []

    for i in range(12):   #appendo un elemento per mese

        diff = 0

        #se considero una lista di 3 anni, ci saranno 2 variazioni
        for k in range(len(lista)-1):    #itero sugli anni
            
            diff = diff + (lista[k+1][i] - lista[k][i])
            #ho sempre come riferimento lo stesso mese[i] ma gli anni [k]progrediscono

        variazione_media = diff/(len(lista)-1)

        lista_finale.append(variazione_media)  
        #alla fine avrò appeso 12 risultati
        #ogni risultato consiste nella media del mese

    return lista_finale
        
    

print("variazione media di passeggeri per mese: {}". format(compute_avg_monthly_difference(time_series, "1950", "1952")))






    
            


   

    