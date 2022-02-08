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

time_series_file = CSVTimeSeriesFile("data.csv")  #istazio l'oggetto

time_series = time_series_file.get_data()
#in questa variabile mi salvo il listone
print(time_series)

def compute_avg_monthly_difference(listone, first_year, last_year):
    #time series è il listone
    #first year è inizio intervallo
    #last year è la fine intervallo

    first_year = int(first_year) -1949
    last_year = int(last_year) -1949


    intervallo_tmp = last_year -first_year +1
    print(intervallo_tmp)

    mucchio = []

    for i,item in listone:     #per ogni mese
        #tutto si volge all'interno di un ciclo for
        
        
        
        #partendo dal primo elemento ficco ogni 12 un elemento nella lista
        for k in range(i, -0, i+12):
            lista = []
            lista.append(listone[i])

        print(lista)

        mucchio.append(lista)

    print(mucchio)

        





compute_avg_monthly_difference(time_series, "1950", "1952")