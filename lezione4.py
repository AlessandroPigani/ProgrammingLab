class Person():

    def __init__(self,arg1,arg2):
        self.name = arg1
        self.surname = arg2

cugino = Person("Pietro","Pigani")   #i due parametri della funzione __init__
#cugino è istanza dell'oggetto Person


print(cugino.name)   #cugino, reparto name
print(cugino.surname)   #cugino, reparto surname


#________________________________________________________________________



class Persona():

    def __init__(self,arg1,arg2):
        self.name = arg1
        self.surname = arg2

    def __str__(self):
        return "Person: {} {}". format(self.name, self.surname) #reparto name e reparto surname

    def saluto(self):
        print("Yo bro, {} here". format(self.name))

person = Persona("Mario", "Rossi")
print(person)   #il metodo str mi fa stampare nome e cognome

#ora estendo la classe Pesrona: creo delle classi figlie che ereditano le caratteristiche dalla classe pasre
#Posso aggiungere metodi oppure sovrascriverli

class Studente(Persona):

    def __str__(self):
        return "Studente: {} {}". format(self.name, self.surname)


class Professore(Persona):

    def __str__(self):
        return "Professore: {} {}". format(self.name, self.surname)

    def saluto(self):            
        print("Goodmorning guys")
        #sovrascrivo il metodo saluto, per avere un saluto più consono

    def saluto_originale(self):
        super().saluto()#recupero il saluto da gangster della classe padre


schugnizzo = Studente("Leonardo", "Bertola")
master = Professore("Gaetano", "Marino")

print(schugnizzo)
schugnizzo.saluto()

print(master)
master.saluto()
master.saluto_originale()
