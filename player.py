class PLAYER():
    def __init__(self, strenght, age, defence, name):
        self.strenght = strenght
        self.age = age
        self.defence = defence  
        self.name = name
        self.is_alive = True

    def print_statistic(self):
        print(f"| Имя: {self.name}")
        print(f"| Сила атаки: {self.strenght}")
        print(f"| Сила защиты: {self.defence}")
        print(f"| Возраст: {self.age}")
    