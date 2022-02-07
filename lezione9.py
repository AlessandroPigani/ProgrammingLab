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

        return aumento_medio

#estendo la classe increment Model
class FitIncrementModel(IncrementModel):
    #vado a implementare il metodo fit

#scrivo praticamente ciò che c'è nella predict di increment model
    def fit(self,data):    #gli darò in pasto i primi 4 mesi
        
        somma = 0
        for i,item in enumerate(data):

            if(i != len(data)-1):

                somma = somma + data[i+1] - data[i]

        res_fit = somma / (len(data)-1)

        self.global_avg_increment = res_fit    #mi sarà utile

        return res_fit 



    
    #sovrascrivo il metodo predict

    def predict(self,data):     #gli darò in pasto gli ultimi mesi

        
        #dilà è l'aumento nei primi mesi
        dilà = self.global_avg_increment  
        #mi salvo in una variabile il risultato della fit
        print("dilà: {}". format(dilà))

        #parental prediction è l'aumento nei primi mesi
        parental_prediction = super().predict(data)
        #recupero direttamente il vslore che mi dà la predict di IncrementModel (classe padre)
    

        plus = (dilà + parental_prediction)/2
        print("aumento medio finale: {}". format(plus))

        risultato = data[-1] + plus

        return risultato

lista = [8,19,31,41,50,52,60]

pippo = FitIncrementModel()

print("primi elementi: {}". format(lista[0:4]))


print("incremento medio sui primi dati: {}". format(pippo.fit(lista[0:4]))) #va fino all'elemento di indice 3  (4 escluso)

print("però dò più peso agli ultimi mesi")
print("ultimi elementi: {}". format(lista[4:7]))

print("perciò la previsione sarà: {}". format(pippo.predict(lista[4:7])))
#va dall'elemento di indice 4 fino all'elemetno di indice 6  (7 escluso)




