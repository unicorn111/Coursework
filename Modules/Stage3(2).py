from city import *

def test_city_add_info():
    inf = City_knowledges(4, ['Kyiv', 'Kharkiv', 'New York', 'Odessa'])
    inf.add_info()
    exp = [['Dniprovskyi District, Kiev', 'Kiev', 'Kiev Voivodeship', 'Solomianka Raion',\
            'Kiev Governorate', 'Embassy of Pakistan, Kiev', 'Maidan Nezalezhnosti',\
            'Viche Maidan (Ivano-Frankivsk)', 'Kiev City Duma building',\
            'Maidan Nezalezhnosti (Kiev Metro)'], ['Kharkiv', 'Statue of Lenin in Kharkiv',\
            'Freedom Square (Kharkiv)', 'Derzhprom (Kharkiv Metro)',\
            'Universytet (Kharkiv Metro)', 'Derzhprom', 'Kharkov Governorate',\
            'Kharkiv National Medical University', 'Zerkalʹnaya struya',\
            'Kharkiv National Automobile and Highway University'],\
           ['Central New York Region', 'New York'], ['Odessa', 'Odessa City Hall',\
            'Odessa Archeological Museum', 'Londonskaya Hotel', 'Maraslis House',\
            'Odessa Funicular', 'Pushkinska Street, Odessa',\
            'Monument to the founders of Odessa', 'Potemkin Stairs',\
                                                     'Odessa Pushkin Museum']]
    if inf == exp:
        return True

def test_city_cities():
    inf = City_knowledges(4, ['Kyiv', 'Kharkiv', 'New York', 'Odessa'])
    inf.add_info()
    a = inf.cities()
    exp = ['Kyiv', 'Kharkiv', 'New York', 'Odessa']
    if a == exp:
        return True

def test_city_add_coord():
    inf = City_knowledges(4, ['Kyiv', 'Kharkiv', 'New York', 'Odessa'])
    inf.add_info()
    inf. add_coord()
    exp = [['Dniprovskyi District, Kiev', 'Kiev', 'Kiev Voivodeship',\
            'Solomianka Raion', 'Kiev Governorate', 'Embassy of Pakistan, Kiev',\
            'Maidan Nezalezhnosti', 'Viche Maidan (Ivano-Frankivsk)',\
            'Kiev City Duma building', 'Maidan Nezalezhnosti (Kiev Metro)',\
            (Decimal('50.4500000000000028421709430404007434844970703125'),\
             Decimal('30.5233333299999998189377947710454463958740234375'))],\
           ['Kharkiv', 'Statue of Lenin in Kharkiv', 'Freedom Square (Kharkiv)',\
            'Derzhprom (Kharkiv Metro)', 'Universytet (Kharkiv Metro)', 'Derzhprom',\
            'Kharkov Governorate', 'Kharkiv National Medical University',\
            'Zerkalʹnaya struya',\
            'Kharkiv National Automobile and Highway University',\
            (Decimal('50.0044444400000003270179149694740772247314453125'),\
             Decimal('36.23138888999999807083440828137099742889404296875'))],\
           ['Central New York Region', 'New York'(Decimal('43'), Decimal('-75'))],\
           ['Odessa', 'Odessa City Hall', 'Odessa Archeological Museum',\
            'Londonskaya Hotel', 'Maraslis House', 'Odessa Funicular',\
            'Pushkinska Street, Odessa', 'Monument to the founders of Odessa',\
            'Potemkin Stairs', 'Odessa Pushkin Museum',\
            (Decimal('46.4857222199999995382313500158488750457763671875'),\
             Decimal('30.743444440000001094404069590382277965545654296875'))]]
    if inf == exp:
        return True

def test_city_info():
    inf = City_knowledges(4, ['Kyiv', 'Kharkiv', 'New York', 'Odessa'])
    inf.add_info()
    a = city_info('Kyiv')
    exp = ['Dniprovskyi District, Kiev', 'Kiev', 'Kiev Voivodeship',\
           'Solomianka Raion', 'Kiev Governorate', 'Embassy of Pakistan, Kiev',\
           'Maidan Nezalezhnosti', 'Viche Maidan (Ivano-Frankivsk)',\
           'Kiev City Duma building', 'Maidan Nezalezhnosti (Kiev Metro)',\
           (Decimal('50.4500000000000028421709430404007434844970703125'),\
            Decimal('30.5233333299999998189377947710454463958740234375'))]
    if a == exp:
        return True       
