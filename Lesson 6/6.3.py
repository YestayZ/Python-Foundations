class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return int(self._income.get('wage')) + int(self._income.get('bonus'))


person = Position('Yestay', 'Zeinollauly', 'ITM Business Interface Engineer', 120000, 20000)
print(f'{person.get_full_name()} works as {person.position} and earns {person.get_total_income()}')
