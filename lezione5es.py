class CSVFile:
    def __init__ (self,name):
        self.name = name

    def get_data(self):
        try:                           #prova a fare questo
            my_file = open(self.name, "r")

       

            listini = []
            for line in my_file:
                riga = line.split(",")
                if(riga[0]!= "Date"):
                    riga[1] = riga[1] [0:-1]

                    listini.append(riga)
                

            my_file.close()

            return listini

            

        except OSError:                        #altrimenti fai questo
            print("eh no, il file non esiste, qui c'è un OSError")
        
       
        except Exception as e:                
            print("c'è un errore")   
            print("ho avuto questo errore: {}". format(e))

giusto = CSVFile("shampoo_sales.txt")
print(giusto.get_data())

errato = CSVFile("proprio luiiii")
print(errato.get_data())

#______________________________________________________________________

print("ora c'è Numerical")

class Numerical(CSVFile):
    def __init__(self,name):
        self.name = name

    def get_data(self):
        
        my_file = open(self.name, "r")

        liste = []

        for line in my_file:
            riga = line.split(",")

            if(riga[0]!="Date"):
            #qua converto in numeri la riga[1]
                
                try:
                    riga[1] = float(riga[1]) 

                    liste.append(riga)

                except Exception as e:
                    print("non posso convertire la parte dopo la virgola in numero")
                    print("non appenderò quella riga")
                

        return liste

        my_file.close()

        

pippo = Numerical("shampoo_sales.txt")
print(pippo.get_data())

pluto = Numerical("shampoo_sales_errori.csv")   #lista alterata
print(pluto.get_data())


#______________________________________________________________________

#il più importamte
print("ora c'è Numericale")


class Numericale(CSVFile):
    def __init__(self,name):
        self.name = name

    def get_data(self):
        
        my_file = open(self.name, "r")

        liste = []

        for line in my_file:
            riga = line.split(",")

            if(riga[0]!="Date"):
                for i,element in enumerate(riga):  #itero sulla riga
                    if(i==0): 
                        liste.append(riga[0])

                    else:
                        try:
                            riga[i] = float(riga[i])

                            liste.append(riga[i])

                        except Exception as e:
                            print("non posso convertire la parte dopo la virgola in numero")
                            print("non appenderò quella riga")
                

        return liste

        my_file.close()

        

        


pippe = Numericale("shampoo_sales.txt")
print("nome del file: {}". format(pippe.name))
print("contenuto del file: {}". format(pippe.get_data()))

plute = Numericale("shampoo_sales_errori.csv")   #lista alterata
print("nome del file: {}". format(plute.name))
print("contenuto del file: {}". format(plute.get_data()))

        

    
    
