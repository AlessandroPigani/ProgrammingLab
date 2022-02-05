#non specifico alcuna eccezione

my_var = "giulia"

try:
    my_var = float(my_var)

except:
    print("non posso fare l'operazione")

print(my_var)

#____________________________________________________________________

#eccezione generica
variabile = "arianna"

try:
    variabile = float(variabile)

except Exception as e:          #la variabile e è l'eccezione
    print("non posso fare l'operazione")
    print("sai qual'è il problema: {}". format(e))


#____________________________________________________________________

#eccezioni assai specifiche

derby = "milan"

try:
    derby = derby.append(4)

except ValueError:
    print("non puoi fare così")
    print("ho avuto un value ValueError")

except TypeError:
    print("non puoi fare così")
    print("ho avuto un TypeError")
 
except AttributeError:      #questa specifica eccezione para l'errore
    print("non puoi fare così") 
    print("ho avuto un AttributeError")

except Exception as e:
    print("non puoi fare così")
    print("ho avuto questo tipo di errore: {}". format(e))

