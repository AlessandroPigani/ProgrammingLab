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

        return aumento_medio   #mi andrò a pescare questo valore nella predict di FitIncrementModel

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

    def predict(self,data):    #ci faccio solo una somma

        
        #c'è solo fit
        risultato = data[-1] + self.global_avg_increment

        return risultato

lista = [8,19,31,41,50,52,60,67,72,79]

n_mesi_controllo = 3

control = lista [-n_mesi_controllo : ]
print("valori per il controllo: {}". format(control))

mesi_fit = lista [0 : - n_mesi_controllo]

print("valori per il modello: {}". format(mesi_fit))

pippo = FitIncrementModel()
print(pippo.fit(mesi_fit))
paperino = pippo.predict(mesi_fit)

print("modello senza controllo: {}". format(paperino))

#itero per fare i controlli e aggiornare la lista dei mesi_fit
for i,element in enumerate(control):
    aumento = pippo.fit(mesi_fit)
    print("aumento medio: {}". format(aumento))

    quo = pippo.predict(mesi_fit)    #quo è la predizione
    print("valore predetto: {}". format(quo))

    scarto = quo - control[i]   #control[i] è il valore effettivo
    print("lo scarto è: {}". format(scarto))

    mesi_fit.append(control[i])  #gonfio la lista dei mesi della fit

    print("next one")

#più si va avanti più i valori per il controllo entrano nella fit e applico l'aumento medio all'ultimo mesi considerato

