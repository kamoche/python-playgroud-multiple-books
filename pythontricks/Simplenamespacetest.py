from types import SimpleNamespace

car1 = SimpleNamespace(color='red',
                       mileage=3812.4,
                       automatic=True)

# >>> car1
# namespace(automatic=True, color='red', mileage=3812.4)

car1.mileage = 12
car1.windshield = 'broken'
del car1.automatic
# >>>car1
# namespace(color='red', mileage=12, windshield='broken')
