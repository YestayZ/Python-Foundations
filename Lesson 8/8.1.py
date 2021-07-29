class Date:
    year = None
    month = None
    day = None

    def __init__(self, dates: str):
        self.dates = dates

    @classmethod
    def extracting(cls, objects):
        return objects.dates.split('-')

    @staticmethod
    def validation(dates):
        days, months, years = map(int, str(dates).split('-'))
        return 'Correct date!' if 1 <= days <= 31 and 1 <= months <= 12 and 1 <= years <= 3999 else 'Wrong date!'


date = '01-01-2021'
print(Date.validation(date))
date_sep = Date(date)
print(date_sep.extracting(date_sep))

