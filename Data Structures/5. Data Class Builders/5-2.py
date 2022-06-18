# NamedTuple For Data class builder

from typing import NamedTuple

class Coordinate(NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'



X = Coordinate(5,6)
Y = Coordinate(5,6)

print(X, Y)
print(X == Y)