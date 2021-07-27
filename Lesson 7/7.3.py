class Cells:

    def __init__(self, qty):
        self.qty = qty

    def __add__(self, other):
        return self.qty + other.qty

    def __sub__(self, other):
        return self.qty - other.qty

    def __mul__(self, other):
        return self.qty * other.qty

    def __truediv__(self, other):
        return self.qty // other.qty

    def ordering(self, in_row):
        rows, tail = self.qty // in_row, self.qty % in_row
        return '\n'.join(['0' * in_row] * rows + (['0' * tail] if tail else []))


cell = Cells(32)
print(cell.ordering(5))