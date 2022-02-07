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

        #ok sono riuscito a creare liste da 12 elementi
        #ma tutto è ancora all'interno del listone
        
    return lista

print(compute_avg_monthly_difference(time_series, "1949", "1960"))


    
            


   

    