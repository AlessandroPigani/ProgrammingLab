class Studente():

    ruolo = "studente units"   #attributo valido sempre nella classe

    def __init__(self,arg1,arg2): 
        #self permette all'attributo di sopravvivere una volta uscito dal metodo
        self.nome = arg1      
        self.cognome = arg2  

    def bonjour(self):    #non aggiungo altri parametri
        print("ecco a voi: {}: {} {}". format(self.ruolo, self.nome, self.cognome))

ciapo = Studente("Giulio", "Caravagna")  
#non serve che specifico il ruolo (tanto è uguale per tutti)

ciapo.bonjour()

print("campo del nome:", ciapo.nome)

ciapo.nome = "Stefano"  #accedo al campo del nome e lo modifico

print("campo del nome modificato:", ciapo.nome)