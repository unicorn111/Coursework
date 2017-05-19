import wikipedia
from arrays import *

class City_knowledge:
    def __init__(self, city):
        self.city = city
        self.crd = ()
        self.info = []

    def coord(self):
        self.crd = wikipedia.WikipediaPage(self.city).coordinates
        return self.crd

    def search_info(self):
        self.info = wikipedia.geosearch(self.crd[0], self.crd[1])
        return self.info

    def __str__(self):
        a = ''
        for i in self.info:
            print(wikipedia.summary(i))
        return'{}'.format(a)


class City_knowledges:
    def __init__(self, city_num, cities):
        self.city_num = city_num
        self.flst = Array(self.city_num + 1)
        self.cities = cities

    def add_info(self):
        num = 0
        for i in self.cities:
            na = City_knowledge(i)
            na1 = na.coord()
            na2 = na.search_info()
            self.flst.__setitem__(num, na2)
            num += 1

    def cities(self):
        return self.cities

    def add_coord(self):
        num = 0
        for i in self.cities:
            na = City_knowledge(i)
            na1 = na.coord()
            self.flst[num].append(na1)
            num +=1

    def city_info(self, city):
        try:
            for i in range(len(self.flst)):
                if city in self.flst[i]:
                    print(self.flst[i])
        except TypeError:
            pass

    def __str__(self):
        a = ''
        for i in range(len(self.flst)):
            print(self.flst[i])
        return'{}'.format(a)
        
