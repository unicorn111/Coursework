from city import *

a = City_knowledges(4, ['Kyiv', 'Kharkiv', 'New York', 'Odesa'])
print(a)
a.add_info()
print(a)
print(a.cities)
a.add_coord()
print(a)
print(a.city_info('Kyiv'))



