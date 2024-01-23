# Паттерны или шаблоны разработки - это общие способы решения частых задач и проблем
# Singleton Одиночка - это шаблон предоставления глобального доступа к состоянию
# нужен для одной точки доступа

class Singleton:
    instance = None

    def __new__(cls):
        if Singleton.instance is None:
            Singleton.instance = super().__new__(cls)
            Singleton._do_work(Singleton.instance)
        return Singleton.instance

    def _do_work(self):
        print('do some hard work')
        self.data = 101


if __name__ == '__main__':
    first = Singleton()
    print(first)
    second = Singleton()
    print(second)
    print(first is second)
