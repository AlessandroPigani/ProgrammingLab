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

        somma = 0
        for i,item in enumerate(data):  #i è l'indice associato ad item
        #item srebbe ogni elemento della lista data
            if(i!=len(data)-1): #mi salta l'indice che sforerebbe
                somma = somma + (data[i+1] - data[i])


        media = somma/(len(data)-1)  
        #len è una funzione che mi misura la lunghezza della lista
        #considero gli n mesi precedenti rispetto a novembre (2) non (3)

        risultato = media + data[-1] 
        #data[-1] mi individua l'ultimo elemento della lista data

        return risultato


pippo = IncrementedModel()
#instanziazione di IncrementedModel

my_list = [50,52,60]

previsione = pippo.predict(my_list)  #self non serve ripeterlo. 
#my_list viene inserito al posto del parametro data

print(previsione)
    




        

                  
            