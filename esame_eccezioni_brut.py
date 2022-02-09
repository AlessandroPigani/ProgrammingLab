#brutta
class ExamException(Exception):

    pass


class CSVTimeSeriesFile():
    
    def __init__(self,arg1):

        self.name = arg1     
        #l'attributo sopravvive all'uscita dalla funzione


    def get_data(self):
        listone = [] #mi preparo una lista in cui inserirò listini di data in stinga e passeggeri in numero
        try:
            my_file = open(self.name,"r")

        except:
            raise ExamException("il file non esiste")

        for line in my_file:
            elements = line.split(",")

            if(elements[0]!="date"):
                
                try:
                    elements[1] = float(elements[1])
                    
                          

                #eccezione quando non riesco a convertire stringhe in numeri
                except ValueError:
                    print("non sono riuscito a convertire la seguente stinga a numero: {}. Ma non importa". format(elements[1]))
                    

                listone.append(elements)       


        my_file.close()

        return listone

time_series_file = CSVTimeSeriesFile("dataerrori.csv")  #istazio l'oggetto

time_series = time_series_file.get_data()
#in questa variabile mi salvo il listone
print(time_series)

#ora ho i dati per fare il vero esercizio

def compute_avg_monthly_difference(time_series, first_year, last_year):
    #time series è il listone
    #first year è inizio intervallo
    #last year è la fine intervallo

    

    for i,element in enumerate(time_series):   #itero sulla lista
        time_series[i] = time_series[i][1]  #considero solo il numero di passaeggeri. non mi servono le date

    #tanto so che ogni 12 valori si passa all'anno successivo

    #spacchettiamo, da un listone devo avere delle liste
    #una lista per anno
    for i,item in enumerate(time_series): #per ogni element in time_series
            
        lista = []   #preparo una lista in cui ogni elemento equivarrà ai valori di un anno
       
                   #start        #stop    #step 
        for i in range(0, len(time_series), 12):   #RIVEDERE PASSAGGIO
            lista.append(time_series[i : i+12])  #appendo da i a i+12
            #appendi le 12 coppie di valori consecutive

    print(lista)   #all'interno del listone ho creato delle liste, ogni lista interna al listone contiene i dati di un anno

    #_________________________________________________________
    #mi dedico agli anni

    #ora mi chiedo se le variabili sono istanza della classe str
    if not isinstance(first_year, str) or not isinstance(last_year, str): 
        raise ExamException("volevo gli anni {} {} sotto forma di stringa". format(first_year, last_year))


    
    #la funzione int me li trasforma in interi
    #non posso mettere float
    #altrimenti mi darebbe errore nello slicing
    try:
        first_year = int(first_year) - 1949  #anno di partenza
        last_year = int(last_year) - 1949

    except:
        raise ExamException("almeno un dei valori corrispondenti alla data non è valido o non è convertibile a numero: {} {}". format(first_year, last_year))

    if(first_year<0 or last_year>11):
        raise ExamException("non abbiamo a disposizione dati relativi a questo intervallo di tempo: {}-{}". format(first_year+1949, last_year+1949))

    if(first_year >= last_year):
        raise ExamException("intervallo di tempo errato o senza senso: {}-{}". format(first_year+1949, last_year+1949)) 
    
     
    print(first_year) #inutile
    print(last_year)
    
    lista = lista [first_year : last_year+1]   #slicing
    #taglio la lista dove mi interessa, gli anni interessati

    print("_________________________________________________________")

    print("dati che mi interessano: {}". format(lista))  #nuova. dove c'è ciò che mi interessa
    print(lista[0])  #benissimo, posso iterare sulla lista per individuar gli anni 

    print("_________________________________________________________")

    
    lista_finale = []

    for i in range(12):   #appendo un elemento per mese

        diff = 0
        

        #se considero una lista di 3 anni, ci saranno 2 variazioni
        for k in range(len(lista)-1):    #itero sugli anni
            
            try:
                diff = diff + (lista[k+1][i] - lista[k][i])
                #ho sempre come riferimento lo stesso mese[i] ma gli anni [k]progrediscono

            except TypeError:  
                print("c'è un dato errato, ma non importa")
                #sommare numeri e stringhe consiste in un TypeError
                #diff non aumenta

                
                 
        
            variazione_media = diff/(len(lista)-1)  #il fatto che manchi un dato incide sul divisore

            #se avevo 2 mesi e uno non lo ho considerato, diff rimane zero (che è una delle richieste del prof)
            #se considero tanti anni ma ho solo una misurazione, diff rimane 0 (TOP)
       

        lista_finale.append(variazione_media)  
        #alla fine avrò appeso 12 risultati
        #ogni risultato consiste nella media del mese

    return lista_finale
        
    

print("variazione media di passeggeri per mese: {}". format(compute_avg_monthly_difference(time_series, 1949, 1960)))