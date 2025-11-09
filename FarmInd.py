class Tomato:
    states = ['цветение', 'зеленый', 'красный']
    
    def __init__(self, index):
        self._index = index
        self._state = self.states[0]
    
    def grow(self):
        current_index = self.states.index(self._state)
        if current_index < len(self.states) - 1:
            self._state = self.states[current_index + 1]
    
    def is_ripe(self):
        return self._state == self.states[-1]

class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(i) for i in range(num_tomatoes)]
    
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()
    
    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)
    
    def give_away_all(self):
        self.tomatoes.clear()


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant
    
    def work(self):
        self._plant.grow_all()
    
    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Урожай собран!")
        else:
            print("Еще не все томаты созрели!")
    
    @staticmethod
    def knowledge_base():
        print("Справка по садоводству: томаты проходят стадии созревания: " \
        "цветение -> зеленый -> красный")


if __name__ == "__main__":
    print("1. Вызов справки по садоводству:")
    Gardener.knowledge_base()
    
    print("\n2. Создание объектов:")
    bush = TomatoBush(3)
    gardener = Gardener("Иван", bush)
    print(f"Создан садовник {gardener.name} с кустом из {len(bush.tomatoes)} томатов")
    
    print("\n3. Уход за кустом:")
    gardener.work()
    print("Проведена первая работа по уходу")
    
    print("\n4. Попытка собрать урожай (томаты еще не дозрели):")
    gardener.harvest()
    
    print("\n5. Продолжение ухода:")
    gardener.work()
    print("Проведена вторая работа по уходу")
    
    print("\n6. Сбор урожая:")
    gardener.harvest()