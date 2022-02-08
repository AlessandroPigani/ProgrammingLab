class ExamException(Exception):

    pass


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

                bit = elements[0].split("-")

                bit[0] = int(bit[0])
                bit[1] = int(bit[0])

                #QUA HO FATTO ESPERIMENTI
                #HO CERCATO DI CONVERTIRE L'ANNO IN VALORE NUMERICO MA È COMPLICATISSIMO DATO CHE C'È ANCHE IL TRATTINO E IL MESE..

                listone.append(elements)  #inserisco nel listone sia elements[0] (le date) sia elements[1] (i passeggeri)

        for i,item in listone:
            if(listone[i][0][0]>listone[i+1][0][0]):
                raise ExamException("dati non ordinati")

        my_file.close()

        return listone

time_series_file = CSVTimeSeriesFile("data.csv")  #istazio l'oggetto

time_series = time_series_file.get_data()
#in questa variabile mi salvo il listone
print(time_series)

for i,element in enumerate(time_series):   #itero sulla lista
    time_series[i] = time_series[i][1]

print(time_series)

#togliere le stinghe? come?
#tagliare i caratteri meglio no ultima spiaggi
#salvarsi solo il valore numerico (ma come?)

