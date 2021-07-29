class Warehouse:
    def __init__(self, title):
        self.title = title
        self._store = {}

    def adding(self, equipment):
        self._store.setdefault(equipment.group_name(), []).append(equipment)
        print(f'На склад {self.title} прибыло оборудование {equipment.group_name(), equipment.name, equipment.vendor} ')

    def extract(self, name):
        if self._store[name]:
            self._store.setdefault(name).pop(0)

    @property
    def store(self):
        return self._store


class Equipment:

    def __init__(self, name, vendor, color, year, price):
        self.name = name
        self.vendor = vendor
        self.color = color
        self.year = year
        self.price = price
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name}, {self.vendor}, {self.color}, {self.year}, {self.price}'


class Printer(Equipment):
    def __init__(self, name, vendor, color, velocity, year, price):
        super().__init__(name, vendor, color, year, price)
        self.velocity = velocity

    def __repr__(self):
        return f'{self.name}, {self.vendor},{self.color}, {self.velocity}, {self.year}, {self.price}'

    @property
    def action(self):
        return 'Принтер печатает.'


class Scanner(Equipment):
    def __init__(self, name, vendor, color, addition, year, price):
        super().__init__(name, vendor, color, year, price)
        self.addition = addition

    @property
    def action(self):
        return 'Сканер сканирует'


class Xerox(Equipment):
    def __init__(self, name, vendor, color, year, price):
        super().__init__(name, vendor, color, year, price)

    @property
    def action(self):
        return 'Копирует'


store = Warehouse('ORG Tech')

hp = Printer('DeskJet ', 'hp', 'White', 33, 2018, 8500)
hp2 = Printer('Laser', 'hp', 'Black', 40, 2020, 9800)
scanner = Scanner('L600', 'EPSON', 'White', '100', 2020, 40000)
store.adding(scanner)
store.adding(hp)
store.adding(hp2)


print(store.store)
store.extract('Scanner')
print(store.store)
