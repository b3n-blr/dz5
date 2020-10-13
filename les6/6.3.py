class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"оклад": wage, "премия": bonus}


class Position(Worker):

    def __init__(self,  name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'ФИО: {self.surname} {self.name}'

    def get_total_income(self):
        return sum(self._income.values())


if __name__ == '__main__':
    human = Position('Илья', 'Ильин', 'рабочий', 3500, 1000)
    print(human.get_full_name())
    print(f'заработная плата: {human.get_total_income()}')
    print(human._income)