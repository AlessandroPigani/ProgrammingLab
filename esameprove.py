lista = [[['1950-01',115.0],['1950-02',126.0],['1950-03',141.0],['1950-04',135.0],['1950-05',125.0],['1950-06',149.0],['1950-07',170.0],['1950-08',170.0],['1950-09',158.0],['1950-10',133.0],['1950-11',114.0],['1950-12',140.0]],[['1951-01',145.0],['1951-02',150.0],['1951-03',178.0],['1951-04',163.0],['1951-05',172.0],['1951-06',178.0],['1951-07',199.0],['1951-08',199.0],['1951-09',184.0],['1951-10',162.0],['1951-11',146.0],['1951-12',166.0]],[['1952-01',171.0],['1952-02',180.0],['1952-03',193.0],['1952-04',181.0],['1952-05',183.0],['1952-06',218.0],['1952-07',230.0],['1952-08',242.0],['1952-09',209.0],['1952-10',191.0],['1952-11',172.0],['1952-12',194.0]]]

lista0 = [115,126,141,135,125,149,170,170,158,133,114,140]
lista1 = [145,150,178,163,172,178,199,199,184,162,146,166]
lista2 = [171,180,193,181,183,218,230,242,209,191,172,194]

listone = []

listone.append(lista0)
listone.append(lista1)
listone.append(lista2)

print(listone)

lista_finale = []

for i in range(12):   #appendo un elemento per mese

    diff = 0

    for k in range(len(listone)-1):    #itero sugli anni
        
        diff = diff + (listone[k+1][i] - listone[k][i])
        #ho sempre come riferimento lo stesso mese[i] ma gli anni [k]progrediscono

    risultato = diff/2

    lista_finale.append(risultato)

print(lista_finale)


#per arrivare a queste condizioni devo togliere la parte in stringa dal mio listone

