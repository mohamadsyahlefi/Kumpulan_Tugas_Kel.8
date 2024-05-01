class Peta:
    def __init__(self):
        self.cityList = {}
    
    def print(self):
        for city in self.cityList:
            print(city, ":",self.cityList[city])
        
    def addcity(self,city):
        if city not in self.cityList:
            self.cityList[city] = []
            return True
        return False
    
    def tambahkanJalan(self,city1,city2):
        if city1 in self.cityList and city2 in self.cityList:
            #di list city2 masukkan city1 
            self.cityList[city2].append(city1)
            #di list city1 masukkan city2
            self.cityList[city1].append(city2)
            return True
        return False

petaJatim = Peta()
petaJatim.addcity("Surabaya")
petaJatim.addcity("Sidoarjo")
petaJatim.addcity("Pasuruan")
petaJatim.addcity("Probolinggo")
petaJatim.addcity("Bondowoso")


petaJatim.tambahkanJalan("Surabaya","Sidoarjo")
petaJatim.tambahkanJalan("Pasuruan","Sidoarjo")
petaJatim.tambahkanJalan("Probolinggo","Pasuruan")
petaJatim.tambahkanJalan("Bondowoso","Probolinggo")
petaJatim.tambahkanJalan("Situbondo","Bondowoso")
petaJatim.tambahkanJalan("Banyuwangi","Situbondo")

petaJatim.print()
