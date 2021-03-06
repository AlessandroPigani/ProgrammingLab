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


                    #se elements[1] è un valore negativo, non posso considerarlo. Allora elements[1] acquiserà il valore standard "valore nullo"
                    if(elements[1]<0):
                        print("non posso considerare il valore: {}". format(elements[1]))
                        elements[1] = "valore_nullo"
                        #questo elemento non sarà considerato nel calcolo della variazione media finale
                                                 

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

    #le date nella lista devono essere rigorosamente ordinate

    #CONTROLLO ANNI
    for i,item in enumerate(time_series):
    #devo mettere una condizione affinchè l'indice non mi "esca" dalla lista
        if(i!=len(time_series)-1):

        #se l'anno dell'elemento successivo è inferiore all'anno dell'elemento precedente, alzo eccezione
            if(int(time_series[i+1][0][0:4])<int(time_series[i][0][0:4])):
                raise ExamException("a un dato anno segue un anno inferiore")


    #CONTROLLO MESI
    for i,item in enumerate(time_series):
        #CONSIDERO SE I MESI SI TROVANO FRA 1 E 12
        #[i] indica il listino, [0] indica la data, [5:] intende i caratteri relativi al mese
        if(int(time_series[i][0][5:])<1 or int(time_series[i][0][5:])>12):
            raise ExamException("mese non esistente, ordine temporale della lista compromesso")


        if(i != len(time_series)-1):
            #uso questa contromisura, poco elegante ma efficace
            #se la i raggiunge l'ultimo elemento non faccio più il controllo, sennò esco dalla lista di 1

            #se ci sono due mesi consecutivi uguali, alzo eccezione
            if(int(time_series[i+1][0][5:])==int(time_series[i][0][5:])):
                raise ExamException("non c'è ordine temporale, ci sono mesi uguali in due elementi consecutivi")
            

            #se il mese succesivo è inferiore al mese precedente
            if(int(time_series[i+1][0][5:]) < int(time_series[i][0][5:])):
                #quando l'anno scatta è chiaro che succede ciò
                #ma se l'anno dell'elemento successivo è uguale all'anno dell'elemento precedente, alzo eccezione
                if(int(time_series[i+1][0][0:4]) == int(time_series[i][0][0:4])):
                    raise ExamException("non c'è ordine nei mesi")

        #FINE DEL CONTROLLO SULLE DATE

    

    for i,element in enumerate(time_series):   #itero sulla lista
        time_series[i] = time_series[i][1]  #considero solo il numero di passaeggeri. non mi servono le date

    #tanto so che ogni 12 valori si passa all'anno successivo

    #da un listone devo avere delle liste
    #una lista per anno
    
            
    lista = []   #preparo una lista in cui ogni elemento equivarrà ai valori di un anno
    
                #start        #stop    #step 
    for i in range(0, len(time_series), 12):   
        lista.append(time_series[i : i+12])  #appendo da i a i+12
        #appendi le 12 coppie di valori consecutive

    print(lista)   #all'interno del listone ho creato delle liste, ogni lista interna al listone contiene i dati di un anno

    #_________________________________________________________
    #mi dedico all'intervallo di anni dati in input

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
        
    

print("variazione media di passeggeri per mese: {}". format(compute_avg_monthly_difference(time_series, "1949", "1950")))