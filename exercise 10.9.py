"""
Определите три класса: Bear, Rabbit и Octothorpe. Для каждого из них определите всего один метод — eats().
Он должен возвращать значения 'berries'
(для Bear), 'clover' (для Rabbit) или 'campers' (для Octothorpe). Создайте
по одному объекту каждого класса и выведите на экран то, что ест указанное
животное.
"""


class Bear:
    def eats(self, berries='bereries'):

        return f'Bear eat {berries}'


class Rabbit:
    def eats(self, clover='clover'):
        return f'Rabbit eat {clover}'


class Octothorpe:
    def eats(self, campers='campers'):
        return f'Octothorpe eat {campers}'


bear = Bear()
rabbit = Rabbit()
octothorpe = Octothorpe()
print(f'{bear.eats()}\n{octothorpe.eats()}\n{rabbit.eats()}')