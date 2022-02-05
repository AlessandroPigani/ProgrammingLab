class CSVFile:
    def __init__ (self,name):
        self.name = name

        if type(self.name) != str:
            raise Exception("mona hai sbagliato")

    def get_data(self, start=None, end=None):

        self.start = start
        self.end = end
        
        
        try:                       #prova a fare questo
            my_file = open(self.name, "r")


            listini = []
            
            for line,element in enumerate(my_file):
                if(line>= self.start and line<=self.end):
                    elementi = line.split(",")
                    if(elementi[0]!= "Date"):

                        elementi[1] = elementi[1] [0:-1]

                        listini.append(elementi)
                

            my_file.close()

            return listini


        except OSError:                        #altrimenti fai questo
            print("eh no, il file non esiste, qui c'è un OSError")
        
       
        except Exception as e:                
            print("c'è un errore")   
            print("ho avuto questo errore: {}". format(e))

         


cartella = CSVFile("shampoo_sales.txt")   
print(cartella.get_data(12, 19))
#quando viene alzata l'eccezione sembra che il programma si schianti ma non è così

