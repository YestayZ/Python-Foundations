class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'\nЗапуск отрисовки.'


class Pen(Stationery):
    def draw(self):
        return f'\nЗапуск отрисовки ручкой.'


class Pencil(Stationery):
    def draw(self):
        return f'\nЗапуск отрисовки карандашом.'


class Handle(Stationery):
    def draw(self):
        return f'\nЗапуск отрисовки маркером.'


ruchka = Pen('Ручка')
karandash = Pencil('Карандаш')
marker = Handle('Маркер')
print(ruchka.draw())
print(karandash.draw())
print(marker.draw())