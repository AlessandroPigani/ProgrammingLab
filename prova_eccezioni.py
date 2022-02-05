class coffee():

    def __init__(self, arg1):
        self.temp = arg1

    def sorseggiamo(self):
        if(self.temp>85):
            raise Exception("mona, scotta")

        elif(self.temp<65):
            raise Exception("è gelato")

        else:
            print("temperatura ottimale")

lavazza = coffee(101)
lavazza.sorseggiamo()


