class ExamException(Exception):

    pass


class CSVTimeSeriesFile():
    
    def __init__(self,arg1):
        #il metodo __init__ serve a instanziare l'oggeto

        self.name = arg1     



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
                        #questa nuova stringa non sarà considerata nel calcolo della variazione media finale ovviamente
                    
                          
                #eccezione quando non riesco a convertire stringhe in numeri
                except ValueError:
                    print("non sono riuscito a convertire la seguente stinga a numero: {}. Ma non importa". format(elements[1]))
                    
                    
                    

                listone.append(elements)       


        my_file.close()

        return listone

time_series_file = CSVTimeSeriesFile("data.csv")  #istazio l'oggetto

time_series = time_series_file.get_data()
#in questa variabile mi salvo il listone
print(time_series)

#ora ho i dati per fare il vero esercizio

def compute_avg_monthly_difference(time_series, first_year, last_year):
    #time series è il listone
    #first year è l'inizio intervallo
    #last year è la fine dell'intervallo

    #le date nella lista devono essere rigorosamente ordinate

    #CONTROLLO ANNI
    for i,item in enumerate(time_series):  #itero sul listone
    #devo mettere una condizione affinchè l'indice non mi "esca" dalla lista
        if(i!=len(time_series)-1):

        #se l'anno dell'elemento successivo è inferiore all'anno dell'elemento precedente, alzo eccezione
            if(int(time_series[i+1][0][0:4])<int(time_series[i][0][0:4])):
                raise ExamException("a un dato anno segue un anno inferiore, ordine temporale compromesso")

    
    #CONTROLLO DEI MESI
    for i,item in enumerate(time_series):  #itero sul listone
        #CONSIDERO SE I MESI SI TROVANO FRA 1 E 12
        #[i] indica il listino, [0] indica la data, [5:] intende i caratteri relativi al mese
        if(int(time_series[i][0][5:])<1 or int(time_series[i][0][5:])>12):
            raise ExamException("mese non esistente, ordine temporale della lista compromesso")


        if(i != len(time_series)-1):
            #uso questa contromisura
            #se la i raggiunge l'ultimo elemento non faccio più il controllo, sennò l'indice esce dalla lista di 1

            #se ci sono due mesi consecutivi uguali, alzo eccezione
            if(int(time_series[i+1][0][5:])==int(time_series[i][0][5:])):
                raise ExamException("non c'è ordine temporale, ci sono mesi uguali in due elementi consecutivi")
            

            #se il mese successivo è inferiore al mese precedente
            if(int(time_series[i+1][0][5:]) < int(time_series[i][0][5:])):
                #quando l'anno scatta è chiaro che succede ciò
                #ma se l'anno dell'elemento successivo è uguale all'anno dell'elemento precedente, alzo l'eccezione
                if(int(time_series[i+1][0][0:4]) == int(time_series[i][0][0:4])):
                    raise ExamException("non c'è ordine nei mesi")

        #FINE DEL CONTROLLO SULLE DATE DEL FILE

    #adesso mi sbarazzo delle date, non mi servono più
    for i,element in enumerate(time_series):   #itero sulla lista
        time_series[i] = time_series[i][1]  #considero solo il numero di passeggeri

    #tanto so che ogni 12 valori si passa all'anno successivo

    #da un listone devo avere delle liste
    #una lista per anno
           
    lista = []   #preparo una lista in cui ogni elemento equivarrà ai valori di un anno
    
                #start        #stop    #step 
    for i in range(0, len(time_series), 12):   
        lista.append(time_series[i : i+12])  #appendo da i a i+12
        #appendi le 12 coppie di valori consecutive

    print(lista)   #all'interno del listone ho creato delle liste, ogni lista interna al listone contiene i dati dei passeggeri di un anno
    #avrò un listone con 12 liste

    #_________________________________________________________
    #mi dedico all'intervallo di anni in input

    #ora mi chiedo se le variabili sono istanza della classe str
    if not isinstance(first_year, str) or not isinstance(last_year, str): 
        raise ExamException("volevo gli anni {} {} sotto forma di stringa". format(first_year, last_year))


    
    #la funzione int me li trasforma in interi
    #non posso mettere float
    #altrimenti mi darebbe errore nello slicing
    try:
        first_year = int(first_year) - 1949  #anno di partenza
        last_year = int(last_year) - 1949    #anno di arrivo

    except:
        raise ExamException("almeno uno dei valori corrispondenti alla data non è valido o non è convertibile a numero intero: {} {}". format(first_year, last_year))

    if(first_year<0 or last_year>11):
        raise ExamException("non abbiamo a disposizione dati relativi a questo intervallo di tempo: {}-{}". format(first_year+1949, last_year+1949))

    if(first_year >= last_year):
        raise ExamException("intervallo di tempo errato o senza senso: {}-{}". format(first_year+1949, last_year+1949)) 
    
     
    #adesso first year e last year hanno un valore compreso fra 0 e 11
    
    lista = lista [first_year : last_year+1]   #slicing
    #taglio la lista dove mi interessa, gli anni interessati

    print("_________________________________________________________")

    print("dati che mi interessano: {}". format(lista))  #nuova. dove c'è ciò che mi interessa
    #posso iterare sulla lista per individuar gli anni 
    #se facessi print(lista[0]) mi stamperei il numero di passeggeri relativi al primo anno

    print("_________________________________________________________")

    
    lista_finale = []

    for i in range(12):   #appendo un elemento per mese

        diff = 0
        

        #se considero una lista di 3 anni, ci saranno 2 variazioni
        for k in range(len(lista)-1):    #itero sugli anni
            
            try:   
                diff = diff + (lista[k+1][i] - lista[k][i])
                #ho sempre come riferimento lo stesso mese[i] ma gli anni [k]progrediscono
                #se considero una stringa ovviamente non posso fare questa operazione

            except TypeError:  
                print("c'è un dato errato, ma non importa")
                #sommare numeri e stringhe consiste in un TypeError
                #diff non aumenta

                                
        
        variazione_media = diff/(len(lista)-1)  
                 
       

        lista_finale.append(variazione_media)  
        #alla fine avrò appeso 12 risultati
        #ogni risultato consiste nella media del mese

    return lista_finale
        


#devo passare in input l'intervallo temporale sottoforma di stringa