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
def tambahkanJalan(self, kota1, kota2, jarak):
        if kota1 in self.cityList and kota2 in self.cityList:
            self.cityList[kota1][kota2] = jarak
            self.cityList[kota2][kota1] = jarak
            return True
        return False

    def hapusJalan(self, kota1, kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            if kota2 in self.cityList[kota1]:
                del self.cityList[kota1][kota2]
                del self.cityList[kota2][kota1]
                return True
        return False

    def djikstra(self, source):
        
        distances = {}
        for city in self.cityList:
            distances[city] = float('inf')
        
        distances[source] = 0
        print (distances)
        # Initialize list of unvisited cities
        unvisited_cities = []
        for city in self.cityList:
            unvisited_cities.append(city)
        #unvisited_cities = list(self.cityList.keys())
        print (unvisited_cities)
        
while unvisited_cities:
            # Find the unvisited city with the smallest distance
            min_distance = float('inf')
            closest_city = None
            #mengiterasi setiap kota yang belum dikunjungi
            for city in unvisited_cities:
                #jika jarak kota lebih kecil dari min_distance
                if distances[city] < min_distance:
                    min_distance = distances[city]
                    closest_city = city
                    
            unvisited_cities.remove(closest_city)

            # Update distances to neighboring cities
            for neighbor, weight in self.cityList[closest_city].items():
                #jika jarak kota terdekat + weight lebih kecil dari jarak kota tetangga
                distance = distances[closest_city] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

        return distances
    
petaIndonesia = Graph()
petaIndonesia.tambahkanKota("Surabaya")
petaIndonesia.tambahkanKota("Sidoarjo")
petaIndonesia.tambahkanKota("Probolinggo")
petaIndonesia.tambahkanKota("Malang")
petaIndonesia.tambahkanKota("Blitar")
petaIndonesia.tambahkanKota("Tulungagung")
petaIndonesia.tambahkanKota("Pacitan")
petaIndonesia.tambahkanKota("Magetan")
petaIndonesia.tambahkanKota("Ngawi")
petaIndonesia.tambahkanKota("Nganjuk")
petaIndonesia.tambahkanKota("Mojokerto")

petaIndonesia.tambahkanJalan("Surabaya","Sidoarjo", 25)
petaIndonesia.tambahkanJalan("Sidoarjo","Probolinggo", 79)
petaIndonesia.tambahkanJalan("Problinggo","Malang", 89)
petaIndonesia.tambahkanJalan("Malang","Blitar", 79)
petaIndonesia.tambahkanJalan("Blitar","Tulungagung", 29)
petaIndonesia.tambahkanJalan("Tulungagung","Pacitan", 133)
petaIndonesia.tambahkanJalan("Pacitan","Magetan", 94)
petaIndonesia.tambahkanJalan("Magetan","Ngawi", 36)
petaIndonesia.tambahkanJalan("Ngawi","Nganjuk", 64)
petaIndonesia.tambahkanJalan("Nganjuk","Mojokerto", 67)
petaIndonesia.tambahkanJalan("Mojokerto","Surabaya", 49)

petaIndonesia.printGraph()
shortest_distances = petaIndonesia.djikstra("Surabaya")
print("Jarak terpendek dari Surabaya ke kota lain:")
for city, distance in shortest_distances.items():
    print(city, ":", distance, "km")
