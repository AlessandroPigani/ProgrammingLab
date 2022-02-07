#darò in pasto al modello i dati già pronti. per questo mi creo un'altra classe. SPEZZETTARSI IL PROBLEMA

class Pesca():
    def __init__(self,name):
        self.name = name

    def get_data(self):
        my_file = open(self.name, "r")

        lista_nuova = []  #mi preparo una lista in cui inserirò valori

        for line in my_file:
            riga = line.split(",")

            if(riga[0]!="Date"):
                riga[1] = float(riga[1])

                lista_nuova.append(riga[1])

        my_file.close()

        return lista_nuova

        

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


class FitIncrementModel(IncrementModel):
    #vado a implementare il metodo fit

#scrivo praticamente ciò che c'è nella predict di increment model
    def fit(self,data):    #gli darò in pasto grana parte dei dati

        
        
        somma = 0
        for i,item in enumerate(data):

            if(i != len(data)-1):

                somma = somma + data[i+1] - data[i]

        res_fit = somma / (len(data)-1)

        self.global_avg_increment = res_fit    
        #mi sarà utile. è l'aumento medio sui primi dati

        return res_fit    #questo sarà qui

    
    def predict(self,data):

        parental_prediction = super().predict(data) #vado a ripescare il return della classe padre

        dilà = self.global_avg_increment

        print("aumento medio sui primi dati: {}". format(dilà))

        print("aumento medio sugli ultimi dati: {}". format(parental_prediction))

        plus = (dilà + parental_prediction)/2
        print("aumento medio finale: {}". format(plus))

        risultato = data[-1] + plus

        return risultato   #questo sarà quo


pippo = Pesca("shampoo_sales.txt")

lista_valori = pippo.get_data()
print(lista_valori)
#ho i valori delle vendite
#non resta che inserirli nella classe Model()

print("valori in pasto al fit: {}". format(lista_valori[0:-3]))

paperino = FitIncrementModel()
qui = paperino.fit(lista_valori[0:-3])   #tutto tranne gli ultimi 3 valori


print("valori in pasto alla predict: {}". format(lista_valori[-3:]))

quo = paperino.predict(lista_valori[-3:])   #gli ultimi 3 valori

print("valore predetto: {}". format(quo))

from matplotlib import pyplot
pyplot.plot(lista_valori + [quo], color="tab:red")
pyplot.plot(lista_valori, color="tab:blue")
pyplot.show()
