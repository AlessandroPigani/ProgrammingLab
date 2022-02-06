class Model():

    def fit(self,data):
        raise Exception("metodo non incrementato")

    def predict(self,data):
        raise Exception("metodo non incrementato")


class IncrementModel(Model):
    def predict(self,data):    #implemento il metodo predict

        
        scarti = 0

        for i,item in enumerate(data):
            
            #ora provo a parare un errore
            if(type(data[i]) == str):
                try:
                    data[i] = float(data[i])
                except ValueError:
                    print("hai sbagliato tipo, DAMMI NUMERI")
                #così se l'utente mi passa delle stringhe, prima provo a traforrmare in numeri, poi se non ci riesco stampo il messaggio di errore
        #parantesi finita


        for i,item in enumerate(data):  #itero nella lista

            #ma torniamo a noi
            if(i != len(data)-1):

                scarti = scarti + data[i+1] - data[i]

        aumento_medio = scarti / (len(data)-1)

        prediction = data[-1] + aumento_medio

        return prediction



lista = [54,56,60.5]
pseudo = ["32","45","89.4"]   #questo riesco a trasformarlo in numeri
caz = ["Mario", "Giulia", "Anna"]    #questo no

pippo = IncrementModel()    #creo un'istanza di IncrementModel


print(pippo.predict(lista))    
#printo la funzione la funzione predict dell'istanza pippo (inserendo i dati della lista)

pluto = IncrementModel()
print(pluto.predict(pseudo))

carota = IncrementModel()
print(pippo.predict(caz))
