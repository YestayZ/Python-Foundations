class Road:
    mass = 25  # масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см
    thickness = 5  # толщина полотна в см

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def count_mass(self):
        return self._length * self._width * self.mass * self.thickness / 1000


road = Road(5000, 20)
print(f'\nМасса асфальта, необходимого для покрытия всего дорожного полотна - {road.count_mass()}')
