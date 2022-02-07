class CSVTimeSeriesFile():
    
    def __init__(self,arg1):

        self.name = arg1     
        #l'attributo sopravvive all'uscita della funzione


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

time_series_file = CSVTimeSeriesFile("data.csv")

time_series = time_series_file.get_data()
#in questa variabile mi salvo il listone
print(time_series)

def compute_avg_monthly_difference(listone, first_year, last_year):
    #time series è il listone
    #first year è inizio intervallo
    #last year è la fine intervallo

    #spacchettiamo da un listone deve avere delle liste
    #una lista per anno
    for i,item in enumerate(listone): #per ogni listino in time_series
        
        
        lista = []
       
                   #start         #stop    #step
        for i in range(0, len(time_series), 12):
            lista.append(listone[i : i+12])

    print(lista)   #all'interno del listone ho creato delle liste, ogni lista interna al listone contiene i dati di un anno

    
    #la funzione int me li trasforma in interi
    #non posso mettere float
    #altrimenti mi darebbe errore nello slicing
    first_year = int(first_year) - 1949  
    last_year = int(last_year) - 1949 
    
     
    print(first_year) #inutile
    print(last_year)
    
    lista = lista [first_year : last_year+1]
    #taglio la lista dove mi interessa

    print("_________________________________________________________")

    print(lista)  #nuova



    #ORA DEVO TROVARE IL MODO DI FARE INTERAGIRE IL DATO DI FEBBRAIO CON FEBBRAIO, IL DATO DI MARZO CON MARZO ETC

    
    

    #sono riuscito a creare una lista per i dati del 1950, una per i dati del 1951, una per i dati del 1952
        
    

compute_avg_monthly_difference(time_series, "1950", "1952")


    
            


   

    