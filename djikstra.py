class Graph:
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
    def hapusKota(self, kotaDihapus):
        if kotaDihapus in self.cityList:
            del self.cityList[kotaDihapus]
            for kota in self.cityList:
                if kotaDihapus in self.cityList[kota]:
                    del self.cityList[kota][kotaDihapus]
            return True
        return False

class Graph:
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
    def hapusKota(self, kotaDihapus):
        if kotaDihapus in self.cityList:
            del self.cityList[kotaDihapus]
            for kota in self.cityList:
                if kotaDihapus in self.cityList[kota]:
                    del self.cityList[kota][kotaDihapus]
            return True
        return False
