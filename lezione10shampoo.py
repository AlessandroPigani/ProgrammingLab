class Pesca():
    def __init__(self,name):
        self.name=name

    lista = []

    def get_data(self):
        my_file = open(self.name,"r")

        for line in my_file:
            riga = line.split(",")

            if(riga[0]!="Date"):
                riga[1] = float(riga[1])
                lista.append(riga[1])
        
        return lista    #me la andrò a prendere per avere solo i valori delle vendite


class Model():

    def fit(self,data):
        raise Exception("metodo non incrementato")

    def predict(self,data):
        raise Exception("metodo non incrementato")


#non mi interessa questa classe, potri anche toglierla
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
    def fit(self,data):    #gli darò in pasto una lista
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


pippo = Pesca("shampoo_sales.txt")

lista = []
lista = pippo.get_data()  
#ADESSO HO UNA LISTA DOVE HO LE VENDITE SOTTO FORMA DI NUMERO
#sono pronto a iniziare

print("ecco i miei dati: {}". format(lista))

#24 dati li do in pasto alla fit, il resto per valutare il modello

dati_fit = []
dati_fit = lista[0:24]  #dal primo al 24°
print("elementi per la costruzione del modello: {}". format(dati_fit))

control = []
control = lista[24:]   #dal 25° al 36°
print("elementi per il controllo del modello: {}". format(control))

paperino = FitIncrementModel()
print("aumento inziziale di esempio: {}". format(paperino.fit(dati_fit)))

predizioni = []  #ci andrò a inserire la lista di predizioni

contatore = 0

for i,item in enumerate(control):
    print("--------------------------------------------------------")

    aumento = paperino.fit(dati_fit)  #aumento medio
    print("aumento medio: {}". format(aumento))

    quo = paperino.predict(dati_fit)   #previsione del prossimo elemento
    print("previsione dato: {}". format(quo))
    predizioni.append(quo)

    print("ma il dato vero è: {}". format(control[i]))   

    scarto = abs(quo - control[i])   #Devo avere il valore assoluto
    print("lo scarto è: {}". format(scarto))

    contatore += scarto

    dati_fit.append(control[i])   #gonfio la lista dati_fit

    print("--------------------------------------------------------")

errore_medio = contatore / len(control)
print("errore medio: {}". format(errore_medio))

from matplotlib import pyplot
pyplot.plot(lista[0:24] + predizioni, color='tab:red')
pyplot.plot(lista, color='tab:blue')
pyplot.show()  

#da ricordarsi che la classe FitIncrementModel viene chiamata 12 volte

#Hahahhaha direi che la vendita di shampoo è poco prevedibile