#ho fatto copia-incolla
class CSVFile():  
    def __init__(self, KJ):  
        self.name = KJ    

    def get_data(self):  
        my_list = []

        try:
            my_file = open(self.name, 'r')  

            for line in my_file:
                riga = line.split(',')  

            
            
                if riga[0] != "Date":
                    riga[1] = riga[1] [0 : -1]
                

                    my_list.append(riga)
        
            my_file.close()

        except OSError:  #errore nell'interagire col sistema (in questo caso apro un file inesistente)
            print('il file "{}" non esiste'.format(self.name))
            print('prova ad aprire un altro file')

        return my_list  #nella lista non ho inserito alcun elemento. Quindi mi ritornerĂ  una lista vuota


pippo = CSVFile('claudiobaglioni.txt') #chiamo un file che non esiste

print(pippo.name)
print(pippo.get_data())    