class Persona:
    def __init__(self,arg1,arg2,arg3):
        self.ruolo = arg1
        self.nome = arg2
        self.cognome = arg3

    def bonjour(self):
        print("il celeberrimo {} {} {}". format(self.ruolo,self.nome,self.cognome))

vecchio = Persona("cacciatore", "Federigo", "Degli Alberighi")
#inizializzo la classe (chiamo il metodo init)

vecchio.bonjour()  #chiamo il metodo

#____________________________________________________________________

#ora creiamo una classe figlia che mi parla della facoltà dei ragazzi

class Studente(Persona):
    #non serve che metta subito "studente" fra i parametri, tanto è sempre uguale: scrivo solo i parametri che cambiano
    def __init__(self,nome,cognome,facoltà):
        super().__init__("Studente", nome, cognome)  #dico il ruolo, il nome e il cognome servendomi del metodo nella classe padre (li recupero)
        self.facoltà = facoltà  #e aggiungo la facoltà

    def bonjour(self):
        Persona.bonjour(self) #chiamo il metodo bonjour della classe padre
        print("Frequenta la facoltà:", self.facoltà)

jesolo = Studente("Filippo", "Bitozzi", "medicina")
                #campo nome    cognome    facoltà
jesolo.bonjour()

cervi = Studente("Lenox", "Kasa", "aida")
cervi.bonjour()