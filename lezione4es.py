class CSVFile():

    def __init__(self,arg1):

        self.name = arg1     
        #l'attributo sopravvive all'uscita della funzione

    def get_data(self):

        lista_nuova = []
        my_file = open(self.name,"r")  #apro l'attributo (che è il file)

        for line in my_file:
            elementi = line.split(",")   #divido le date dai valori

            if(elementi[0]!="Date"):
                elementi[1] = elementi[1] [0:-1]  
                #taglio l'ultimo carattere dai valori (\n)

                lista_nuova.append(elementi)
        #una volta che ho inserito i 2 elementi nella lista_nuova, questa lista si chiude. E gli elementi successivi entreranno in una nuova lista

        my_file.close()
                

        return lista_nuova

#istanza
goal = CSVFile("shampoo_sales.txt")  #inizializzo il metodo init

print(goal.get_data())  #chiamo il metodo get data
