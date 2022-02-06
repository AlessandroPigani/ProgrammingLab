class CSVFile:
    def __init__ (self,name):
        self.name = name

        if type(self.name) != str:  #se il file non è una stringa alza ecc
            raise Exception("mona hai sbagliato")


    def get_data(self, start=None, end=None):

        self.start = start
        self.end = end

        if(start==None): 
            self.start = 0

        if start<0:
            self.start = 0
    

        listini = []
        
        
        try:  
            if end is not None:                   
                my_file = open(self.name, "r").readlines()[self.start : self.end+1]   #aumento di uno sennò mi taglia l'ultimo
                #leggimi le righe da start a end
            
            else:   #se non specifico end, vado avanti fino alla fine
                my_file = open(self.name, "r").readlines()[self.start : ]

            
            for line in my_file:
                riga = line.split(",")

                if(riga[0]!="Date"):
                    riga[1] = riga[1] [0:-1]

                    listini.append(riga)
                          

            return listini

            my_file.close()
            
            
            
        except OSError:                        #altrimenti fai questo
            print("eh no, il file non esiste, qui c'è un OSError")
                
            
        except Exception as e:                
            print("c'è un errore")   
            print("ho avuto questo errore: {}". format(e))



        
         


cartella = CSVFile("shampoo_sales.txt")   
print(cartella.get_data(12,15))
#quando viene alzata l'eccezione sembra che il programma si schianti ma non è così

