class Model():

    def fit(self,data):
        raise Exception("metodo non incrementato")

    def predict(self,data):
        raise Exception("metodo non incrementato")


class IncrementModel(Model):
    def predict(self,data):    #implemento il metodo predict

        
        scarti = 0

        for i,item in enumerate(data):  #itero nella lista 

            if(i != len(data)-1):

                scarti = scarti + data[i+1] - data[i]

        aumento_medio = scarti / (len(data)-1)

        prediction = data[-1] + aumento_medio

        return prediction


#estendo la classe increment Model
class FitIncrementModel(IncrementModel):
    #vado a implementare il metodo fit

#scrivo praticamente ciò che c'è nella oredict di increment model
    def fit(self,data):
        
        somma = 0
        for i,item in enumerate(data):

            if(i != len(data)-1):

                somma = somma + data[i+1] - data[i]

        res_fit = somma / (len(data)-1)

        return res_fit   #mi sarà utile



    
    #sovrascrivo il metodo predict

    def predict(self,data):

        dilà = self.fit(data)  
        #mi salvo in una variabile il risultato della fit


        scarti = 0

        for i,item in enumerate(data):
            
            #considero solo gli ultimi valori
            if(i >= len(data)-3 and i<(len(data)-1)):

                scarti = scarti + data[i+1] - data[i]

        aumento = scarti / ((len(data)-1) - (len(data)-3))


    

        plus = (dilà + aumento)/2

        risultato = data[-1] + plus

        return risultato

lista = [8,19,31,41,50,52,60]

pippo = FitIncrementModel()


print("incremento medio su tutti i dati: {}". format(pippo.fit(lista)))
print("però dò più peso agli ultimi mesi")
print("perciò la previsione sarà: {}". format(pippo.predict(lista)))

        

        




