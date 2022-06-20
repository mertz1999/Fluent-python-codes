# Destructuring nested tuples

metro_areas = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
        (1234, 'BR', 19.649, (-23.547778, -46.635833)),
              ]

# print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
for record in metro_areas:
    match record:
        case [str(name), _, _, (lat, lon)] if lon <= 0:
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')
        
        case [int(name), _, _, _]:
            print("Name is not correct!")



# case [str(name), *_, (float(lat), float(lon))]
