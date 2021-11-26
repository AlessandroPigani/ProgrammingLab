class CSVfile():  #questo è un oggetto (classe)
    def __init__(self, KJ):  #chiamo la funzione init perchè viene eseguita quando inizializzo/ instanzio
        self.name = KJ     #self.name è un attributo
#l'attributo name sarà uguale al parametro kj
#prendo in input una variabile 
#la variabile name sarà associata al parametro name (grazie a self.name)


#la seguente funzione (trovandosi dentro un oggetto) si chiama metodo
    def get_data(self):  
        my_list = []
        my_file = open(self.name, 'r')   #apro file in lettura mode

        for line in my_file:
            riga = line.split(',')  

            #insomma riga è una lista contiene elementi di indice 0 (le date) e di indice 1 (i prezzi)
            #Ho tanti piccoli listini, con ognuno una coppia di elementi
            
            if riga[0] != "Date":
                riga[1] = riga[1] [0 : -1]
                #alla riga di indice 1 (cioè i prezzi) non considerererò l'ultimo vado carattere (vado dal carattere di indice 0 a -1). Taglio la riga di indice 1 (taglio \n)

                my_list.append(riga) #mi insrisce in my_list ogni riga apparte "Date Sales" (perchè ho messo la condizione)

                #quindi all'interno della lista my_list ho inserito ogni riga (apperte la prima)
                #riga è un elemento dal punto di vista del my_list

        my_file.close()

        return my_list


pippo = CSVfile('shampoo_sales.txt')

print(pippo.name)
print(pippo.get_data())

            
            
               
        
        