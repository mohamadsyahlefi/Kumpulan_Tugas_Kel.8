from itertools import permutations

class WeightedGraph:
    #initialization
    def __init__(self):
        self.cityList = {}

    def printGraph(self):
        #mengiterasi setiap city
        for city in self.cityList:
            #setiap kota print nama kota
            print(city, ":", self.cityList[city])

            # Print distances to neighboring cities
            for neighbor, distance in self.cityList[city].items():
                #print tetangga dan jarak
                print("    ->", neighbor, ":", distance)

    def tambahkanKota(self, kota):
        #jika kota tidak ada di cityList
        if kota not in self.cityList:
            #maka tambahkan kota
            self.cityList[kota] = {}
            return True
        return False

    def tambahkanJalan(self, kota1, kota2, jarak):
        if kota1 in self.cityList and kota2 in self.cityList:
            self.cityList[kota1][kota2] = jarak
            self.cityList[kota2][kota1] = jarak
            return True
        return False

petaJatim = WeightedGraph()
petaJatim.tambahkanKota("Surabaya")
petaJatim.tambahkanKota("Sidoarjo")
petaJatim.tambahkanKota("Pasuruan")
petaJatim.tambahkanKota("Probolinggo")
petaJatim.tambahkanKota("Bondowoso")
petaJatim.tambahkanKota("Situbondo")
petaJatim.tambahkanKota("Banyuwangi")
petaJatim.tambahkanKota("Jember")
petaJatim.tambahkanKota("Lumajang")
petaJatim.tambahkanKota("Malang")
petaJatim.tambahkanKota("Tulungagung")
petaJatim.tambahkanKota("Kediri")

petaJatim.tambahkanJalan("Surabaya","Sidoarjo", 33)
petaJatim.tambahkanJalan("Pasuruan","Sidoarjo", 40)
petaJatim.tambahkanJalan("Probolinggo","Pasuruan", 40)
petaJatim.tambahkanJalan("Bondowoso","Probolinggo", 111)
petaJatim.tambahkanJalan("Situbondo","Bondowoso", 36)
petaJatim.tambahkanJalan("Banyuwangi","Situbondo", 95)
petaJatim.tambahkanJalan("Jember","Banyuwangi", 104)
petaJatim.tambahkanJalan("Lumajang","Jember", 64)
petaJatim.tambahkanJalan("Malang","Lumajang", 91)
petaJatim.tambahkanJalan("Tulungagung","Malang", 108)
petaJatim.tambahkanJalan("Kediri","Tulungagung", 31)
petaJatim.tambahkanJalan("Surabaya","Kediri", 129)

petaJatim.printGraph()