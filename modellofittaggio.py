class Model():

    def fit(self,data):
        # Fit non implementanto nella classe base
        raise NotImplentedError('Metodo non implementanto')

    def predict(self,data):
        # Predict non implementanto nella classe base
        raise NotImplentedError('Metodo non implementanto')
        #anche se in realtà NotImplentedError non è un'eccezione built in.
        #Forse converrebbe mettere un generico exception


class IncrementedModel(Model): #implemento (definisco) la funzione predict

#non sto richiamando la funzione predict. La sto ridefinendo
    def predict(self,data):

        somma_incrementi = 0
        for i,item in enumerate(data):  #i è l'indice associato ad item
        #item srebbe ogni elemento della lista data
            if(i!=len(data)-1): #mi salta l'elemento con ultimo indice
                somma_incrementi = somma_incrementi + (data[i+1] - data[i])


        media_incremento = somma_incrementi/(len(data)-1)  
        #len è una funzione che mi misura la lunghezza della lista
        #considero gli n mesi precedenti rispetto a novembre (2) non (3)

        risultato = media_incremento + data[-1] 
        #data[-1] mi individua l'ultimo elemento della lista data

        return risultato


pippo = IncrementedModel()
#instanziazione di IncrementedModel

my_list = [50,52,60]

previsione = pippo.predict(my_list)  #self non serve ripeterlo. 
#my_list viene inserito al posto del parametro data

print(previsione)

#ok, ora cominciamo il vero esercizio di oggi: implementare il metodo fit

class FitIncrementModel(IncrementedModel): #estensione

    def fit(self,data):
        somma_incrementi = 0
        for i,item in enumerate(data):  #i è l'indice associato ad item
        #item srebbe ogni elemento della lista data
            if(i!=len(data)-1): #mi salta l'elemento con ultimo indice
                somma_incrementi = somma_incrementi + (data[i+1] - data[i])


        media_incremento = somma_incrementi/(len(data)-1)  
        #len è una funzione che mi misura la lunghezza della lista
        #considero gli n mesi precedenti rispetto a novembre (2) non (3)

        self.global_avg_increment = media_incremento
        #l'attributo global_avg_increment deve avere self. davanti affinchè possa sopravvivere ancheuna volta usciti da questo metodo

    #insomma nella fit mi calcolo l'incremento medio di tutti gli elementi della lista (in questo caso).
    #In realtà a mia discrezione, sono io che decido quanto peso dare alla funzione fit e quanto peso dare alla funzione predict.
    #In questo caso ho deciso di valutare tutti i dati

    
    #sovrascrivo il metodo Predict
    def predict(self,data):
        
        return self.global_avg_increment + data[-1]
        #insomma ma ritorna l'incremento medio associato all'ultimo valore

    #la predict insomma sfrutta il piatto d'argento che le viene servito dalla fit

minnie = FitIncrementModel()

lista = [8, 19, 31, 41, 50, 52, 60]

minnie.fit(lista)
#ho chiamato la funzione fit (è necessario)

#chiamo anche la funzione predict nel momento associo l'istanza a una variabile
previsione_fit = minnie.predict(lista)
print("con fit",previsione_fit)