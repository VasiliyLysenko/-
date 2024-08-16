class Building:
    def __init__(self):
        self.total = 1

buildings = [Building() for _ in range(40)]
for building in buildings:
    print(f'Создано строение')
